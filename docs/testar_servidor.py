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
    corpo = "Bloco de aula com conteúdo suficiente para a validação de extensão mínima. " * 6
    blocos = [
        {"type": "conceito", "heading": "Conceito", "body": corpo, "columns": [], "rows": [], "timeline": []},
        {
            "type": "pegadinha",
            "heading": "Pegadinha",
            "body": corpo,
            "columns": [],
            "rows": [],
            "timeline": [],
        },
        {
            "type": "tabela",
            "heading": "Quadro",
            "body": "",
            "columns": ["A", "B"],
            "rows": [["x", "y"]],
            "timeline": [],
        },
    ]
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
            "lessons": [{"title": "1. Um", "blocks": blocos}, {"title": "2. Dois", "blocks": blocos}],
            "laws": [],
            "jurisprudence": [],
            "traps": ["t"],
            "mindmap_titulo": "m",
            "mindmap": [],
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
                return e.code, json.loads(e.read() or b"{}")

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
