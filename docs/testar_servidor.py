#!/usr/bin/env python3
"""testar_servidor.py — prova o servidor dos blocos de 30 SEM chamar a API paga e SEM ler o .env.

Copia o servidor.py e os assets versionados para uma pasta temporária (sem .env — HARNESS §F59) e
troca só o `post_json` por uma API falsa: assim o caminho real de `call_model` roda, inclusive a
medição de tokens. Cobre (31/10/2026, D-005 a D-007):

  1. a geração grava `metricas` (chamadas, tokens, duração) e filtra os correlatos (id inventado,
     o próprio ponto e repetição saem);
  2. POST /api/bloco enfileira e GET /api/bloco conta; bloco acima de 30 é recusado;
  3. POST /api/historico grava o arquivo único; HTML inválido e origem estranha são recusados.

Uso: python docs/testar_servidor.py   (0 = tudo certo, 1 = falha)
"""

from __future__ import annotations

import importlib.util
import json
import os
import shutil
import socket
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ASSETS_VERSIONADOS = [
    "items.json",
    "banco_inicial.json",
    "catalogo_leis.json",
    "sumulas.json",
    "teses_rg.json",
    "acervo_oficial_curado.json",
]
falhas: list[str] = []


def prova(desc: str, ok: bool, detalhe: str = "") -> None:
    print(f"  {'✅' if ok else '❌'} {desc}" + (f" — {detalhe}" if detalhe and not ok else ""))
    if not ok:
        falhas.append(desc)


def itens_ce(n: int = 10) -> list[dict]:
    """Itens Certo/Errado válidos (v9, 31/10/2026): metade C, metade E, três tipos."""
    tipos = ["doutrina", "lei_seca", "jurisprudencia"]
    return [
        {
            "afirmacao": f"Afirmação {i} de prova sobre o instituto, com extensão suficiente para julgar.",
            "gabarito": "C" if i % 2 else "E",
            "tipo": tipos[i % 3],
            "comentario": f"Comentário {i}: explica por que a afirmação está certa ou errada, "
            "com a versão correta.",
            "fundamento": "CP, art. 1º",
        }
        for i in range(n)
    ]


def questao_valida(correlatos: list[str]) -> dict:
    """Uma questão que passa no validate() do servidor."""
    alt = {
        L: f"Alternativa {L}: afirmação jurídica plausível sobre o instituto, de extensão parecida."
        for L in "ABCDE"
    }
    com_alt = {
        L: {
            "veredito": "Correta" if L == "A" else "Errada",
            "titulo": "aplica o instituto",
            "explicacao": "Explicação objetiva da alternativa, citando o dispositivo legal que a resolve.",
        }
        for L in "ABCDE"
    }
    return {
        "formato": "direta",
        "stem": "Enunciado de teste com extensão suficiente para a validação formal do servidor do Trilha.\n"
        "Considerando a legislação, assinale a alternativa correta.",
        "options": alt,
        "correct": "A",
        "tag": "t",
        "difficulty": "média",
        "source_scope": "teste",
        "commentary": {
            "summary": "s",
            "alternatives": com_alt,
            "certo_errado": itens_ce(),
            "laws": [],
            "jurisprudence": [],
            "gaps": [],
            "itens_correlatos": correlatos,
            "auditoria": {"checklist": [], "cobertura": "c", "fundamento_edital": "f"},
        },
    }


def revisao_valida(correlatos: list[str], n: int = 14) -> dict:
    """Uma revisão C/E (v10) que passa no _checar_revisao(): 12 a 20 itens, cada um com título curto."""
    return {
        "difficulty": "alto",
        "commentary": {
            "summary": "s",
            "certo_errado": [dict(x, titulo="troca o prazo de dez por quinze dias") for x in itens_ce(n)],
            "laws": [],
            "jurisprudence": [],
            "gaps": [],
            "itens_correlatos": correlatos,
            "auditoria": {"checklist": [], "cobertura": "c", "fundamento_edital": "f"},
        },
    }


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # §A7
    tmp = Path(tempfile.mkdtemp(prefix="trilha_teste_"))
    try:
        shutil.copy2(RAIZ / "servidor.py", tmp / "servidor.py")
        (tmp / "assets").mkdir()
        for a in ASSETS_VERSIONADOS:
            if (RAIZ / "assets" / a).exists():
                shutil.copy2(RAIZ / "assets" / a, tmp / "assets" / a)
        with socket.socket() as s:
            s.bind(("127.0.0.1", 0))
            porta = s.getsockname()[1]
        # Determinístico: o servidor audita com o OUTRO provedor quando as duas chaves existem, e o
        # ambiente de quem roda o teste pode ter uma chave real (31/10/2026: herdou e mudou o caminho).
        os.environ.pop("ANTHROPIC_API_KEY", None)
        os.environ.update({"PORT": str(porta), "OPENAI_API_KEY": "valor-falso-de-teste", "DEEP_AUDIT": "1"})
        spec = importlib.util.spec_from_file_location("servidor_teste", tmp / "servidor.py")
        srv = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(srv)

        itens = [t for t in srv.ITEMS if t["discipline"] == "DIREITO PENAL"]
        alvo, vizinho, outro = itens[3]["id"], itens[4]["id"], itens[5]["id"]
        correlatos_brutos = [vizinho, "INVENTADO-99", alvo, vizinho]

        def post_json_falso(url, payload, headers, timeout=240):
            sistema = str(payload.get("instructions") or payload.get("system") or "")
            if sistema.startswith("Você é auditor"):
                texto = json.dumps({"approved": True, "problems": [], "reason": "ok"})
            elif "=== REVISÃO RÁPIDA CERTO/ERRADO" in sistema:  # revisão C/E do bloco (v10, 01/11/2026)
                texto = json.dumps(revisao_valida([vizinho]), ensure_ascii=False)
            elif sistema.startswith("Você é professor de cursinho"):  # conversão para Certo/Errado (v9)
                texto = json.dumps({"certo_errado": itens_ce(12)}, ensure_ascii=False)
            else:
                texto = json.dumps(questao_valida(correlatos_brutos), ensure_ascii=False)
            uso = {"input_tokens": 1000, "output_tokens": 300}
            if "anthropic" in url:  # formato da API da Anthropic
                return {"content": [{"type": "text", "text": texto}], "usage": uso}
            return {"output": [{"content": [{"type": "output_text", "text": texto}]}], "usage": uso}

        srv.post_json = post_json_falso

        # 1. geração: métricas e correlatos
        q = srv.generate(alvo, 1, "openai")
        m = q.get("metricas", {})
        prova("geração grava métricas: 2 chamadas (questão + auditoria)", m.get("chamadas") == 2, str(m))
        prova(
            "tokens somados (2.000 entrada · 600 saída)",
            m.get("tokens_entrada") == 2000 and m.get("tokens_saida") == 600,
            str(m),
        )
        prova(
            "duração e data registradas",
            isinstance(m.get("duracao_s"), float) and bool(m.get("gerada_em")),
            str(m),
        )
        prova(
            "correlatos filtrados: só o id válido, sem o próprio ponto nem repetição",
            q["commentary"]["itens_correlatos"] == [vizinho],
            str(q["commentary"]["itens_correlatos"]),
        )
        prova("arquivo da questão gravado no cache", srv.file_for(alvo, 1).exists())
        prova(
            "a questão nova já nasce com Certo/Errado",
            srv.validar_ce(q["commentary"].get("certo_errado")) is None,
        )

        # 1b. regras do Certo/Errado (v9)
        prova("C/E: 7 itens é pouco", srv.validar_ce(itens_ce(7)) is not None)
        so_certos = [dict(x, gabarito="C") for x in itens_ce(10)]
        prova("C/E: só certos é recusado (tem de misturar)", srv.validar_ce(so_certos) is not None)
        um_tipo = [dict(x, tipo="doutrina") for x in itens_ce(10)]
        prova("C/E: um tipo só é recusado", srv.validar_ce(um_tipo) is not None)
        # 31/10/2026 (CON-2): ponto puramente teórico, sem lei nem jurisprudência — exigir 2 tipos forçaria
        # a IA a inventar fonte. Sem fonte no comentário, só doutrina é aceito; com fonte, continua recusado.
        prova(
            "C/E: sem lei nem jurisprudência, o comentário não 'tem fonte'",
            srv.tem_fonte({"laws": []}) is False,
        )
        prova(
            "C/E: ponto teórico (sem fonte) aceita itens só de doutrina",
            srv.validar_ce(um_tipo, srv.tem_fonte({"laws": [], "jurisprudence": []})) is None,
        )
        prova(
            "C/E: com lei citada, um tipo só continua recusado",
            srv.validar_ce(um_tipo, srv.tem_fonte({"laws": [{"diploma": "CF"}]})) is not None,
        )

        # 1c. conversão de questão ANTIGA: a questão não muda, a aula fica guardada
        antiga = questao_valida([])
        antiga["commentary"].pop("certo_errado")
        antiga["commentary"].update({"lessons": [{"title": "1. Aula", "blocks": []}], "traps": ["p"]})
        arq_antigo = srv.file_for(outro, 2)
        arq_antigo.write_text(json.dumps(antiga, ensure_ascii=False), encoding="utf8")
        srv.converter_ce(arq_antigo, "openai")
        conv = json.loads(arq_antigo.read_text("utf8"))
        prova("conversão: ganha 12 itens Certo/Errado", len(conv["commentary"].get("certo_errado", [])) == 12)
        prova(
            "conversão: enunciado, alternativas e gabarito INTACTOS",
            all(conv[k] == antiga[k] for k in ("stem", "options", "correct")),
        )
        prova(
            "conversão: a aula antiga fica guardada em aula_original (nada se apaga)",
            conv["commentary"].get("aula_original", {}).get("lessons") == antiga["commentary"]["lessons"]
            and "lessons" not in conv["commentary"],
        )
        prova("conversão: mede a chamada", conv.get("metricas_conversao", {}).get("chamadas") == 1)

        # 1d. revisão rápida Certo/Errado (v10, 01/11/2026): o titular escolhe, por assunto, revisar em C/E
        rev_id = itens[6]["id"]
        rv = srv.generate(rev_id, 1, "openai", [], "ce")
        prova(
            "revisão C/E: grava formato revisao_ce com 14 itens",
            rv.get("formato") == "revisao_ce" and rv.get("n_itens") == 14,
            str(rv.get("formato")),
        )
        prova(
            "revisão C/E: sem letra de gabarito (não há alternativas)",
            "correct" not in rv and "options" not in rv,
        )
        prova(
            "revisão C/E: auditoria dupla mantida (2 chamadas: revisão + auditor)",
            rv.get("metricas", {}).get("chamadas") == 2,
            str(rv.get("metricas")),
        )
        prova(
            "revisão C/E: itens com título curto (padrão das alternativas)",
            all(x.get("titulo") for x in rv["commentary"]["certo_errado"]),
        )
        prova("revisão C/E: 11 itens é pouco", srv._checar_revisao(revisao_valida([], 11)) is not None)
        sem_titulo = revisao_valida([])
        sem_titulo["commentary"]["certo_errado"][0]["titulo"] = ""
        prova("revisão C/E: item sem título é recusado", srv._checar_revisao(sem_titulo) is not None)
        prova(
            "prompt da banca cobra o detalhe da letra da lei em todas as disciplinas",
            "LETRA DA LEI EM TODAS AS DISCIPLINAS" in srv.SYS
            and "LETRA DA LEI EM TODAS AS DISCIPLINAS" in srv.REV_SYS,
        )

        # 2 e 3. HTTP
        httpd = srv.http.server.ThreadingHTTPServer(("127.0.0.1", porta), srv.Handler)
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{porta}"

        def chamar(caminho, corpo=None, origem=None):
            dados = json.dumps(corpo).encode() if corpo is not None else None
            req = urllib.request.Request(
                base + caminho,
                data=dados,
                method="POST" if dados else "GET",
                headers={"Content-Type": "application/json", **({"Origin": origem} if origem else {})},
            )
            try:
                with urllib.request.urlopen(req, timeout=10) as r:
                    return r.status, json.loads(r.read())
            except urllib.error.HTTPError as e:
                # O STATUS é o que se confere. Ler o corpo do erro de uma requisição GRANDE recusada travou
                # 2 vezes em 15 no Windows (31/10/2026) com o 403 já recebido — causa exata não identificada.
                try:
                    return e.code, json.loads(e.read() or b"{}")
                except (TimeoutError, OSError, ValueError):
                    return e.code, {}

        st, r = chamar(
            "/api/bloco", {"ids": [vizinho, outro, "INVENTADO-1"], "round": 1, "provider": "openai"}
        )
        prova(
            "POST /api/bloco enfileira os válidos e conta os ignorados",
            st == 200 and r.get("pedidos") == 2 and r.get("ignorados") == 1,
            f"{st} {r}",
        )
        prontos = 0
        for _ in range(50):
            st, r = chamar(f"/api/bloco?round=1&ids={vizinho},{outro}")
            prontos = r.get("contagem", {}).get("ready", 0)
            if prontos == 2:
                break
            time.sleep(0.2)
        prova("GET /api/bloco conta as 2 questões prontas", prontos == 2, str(r))
        st, r = chamar("/api/reveal", {"id": rev_id, "round": 1, "choice": "C/E"})
        prova(
            "POST /api/reveal da revisão devolve os itens comentados (sem exigir letra A–E)",
            st == 200
            and r.get("formato") == "revisao_ce"
            and len(r.get("commentary", {}).get("certo_errado", [])) == 14,
            f"{st} {str(r)[:200]}",
        )
        rev2 = itens[8][
            "id"
        ]  # o itens[7] (PEN-2.2) já está no banco inicial como objetiva: o que está pronto não se regera
        st, r = chamar("/api/bloco", {"ids": [rev2], "round": 1, "provider": "openai", "modos": {rev2: "ce"}})
        for _ in range(50):
            if srv.stored(srv.jobkey(rev2, 1)):
                break
            time.sleep(0.2)
        prova(
            "POST /api/bloco com modos: o ponto marcado 'ce' é gerado como revisão",
            (srv.stored(srv.jobkey(rev2, 1)) or {}).get("formato") == "revisao_ce",
        )
        st, r = chamar("/api/bloco", {"ids": [t["id"] for t in srv.ITEMS[:31]], "round": 1})
        prova("bloco com 31 pontos é recusado (400)", st == 400, f"{st} {r}")

        html_teste = "<!doctype html><html><body>" + ("histórico " * 40_000) + "</body></html>"
        st, r = chamar("/api/historico", {"html": html_teste})
        arq = tmp / "historico" / "Trilha_historico_acumulado.html"
        prova(
            "POST /api/historico grava ~400 KB (antes o limite de 100 KB descartava calado)",
            st == 200 and arq.exists() and arq.read_text("utf8") == html_teste,
            f"{st} {r}",
        )
        st, _ = chamar("/api/historico", {"html": "não é html"})
        prova("histórico que não é HTML é recusado (400)", st == 400)
        # Corpo pequeno de propósito: o servidor recusa a origem SEM ler o corpo, e com 400 KB o Windows
        # derruba a conexão enquanto o cliente ainda envia (medido em 31/10/2026) — a recusa vale igual.
        st, _ = chamar(
            "/api/historico", {"html": "<!doctype html><p>x</p>"}, origem="https://site-estranho.example"
        )
        prova("origem estranha é recusada (403)", st == 403)
        # O caso que derrubava a conexão (31/10/2026): recusa de origem COM corpo grande. O servidor agora
        # lê e descarta o corpo antes de responder, e a recusa chega inteira.
        st, _ = chamar("/api/historico", {"html": html_teste}, origem="https://site-estranho.example")
        prova("origem estranha com corpo de ~400 KB também recebe o 403 (sem conexão derrubada)", st == 403)
        httpd.shutdown()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print()
    print(f"❌ {len(falhas)} falha(s)" if falhas else "✅ servidor verde — geração, bloco e histórico")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
