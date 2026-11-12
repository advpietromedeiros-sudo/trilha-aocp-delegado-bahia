"""Olho de Águia — junta o que os redatores geraram (em .scratch/olho/) nos arquivos que o app lê.

- Pegadinhas: .scratch/olho/peg/out/*.json  ->  revisao/material/olho/pegadinhas.json (acumula; fora do Git)
- Simulados:  .scratch/olho/out/*.json      ->  revisao/material/olho/simulados_marcas.json e
                                                discursiva/olho_aguia_simulados.js (fora do Git: deriva dos Simulados Delta, D-017)
Só entra lote que passa no validador. Depois roda o montador das assertivas.
Uso: python -I ferramentas/olho_de_aguia/juntar.py
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parents[2]
SCR = RAIZ / ".scratch" / "olho"
MAT = RAIZ / "revisao" / "material" / "olho"
MAT.mkdir(parents=True, exist_ok=True)


def valido(validador: Path, lote: str) -> bool:
    return subprocess.run([sys.executable, "-I", str(validador), lote], capture_output=True).returncode == 0


# pegadinhas
arq_peg = MAT / "pegadinhas.json"
peg = json.loads(arq_peg.read_text(encoding="utf-8")) if arq_peg.exists() else {}
for f in sorted((SCR / "peg" / "out").glob("*.json")):
    if valido(SCR / "peg" / "validar.py", f.stem):
        peg.update(json.loads(f.read_text(encoding="utf-8")))
    else:
        print(f"pegadinhas: lote {f.stem} reprovado no validador, ficou de fora")
arq_peg.write_text(json.dumps(peg, ensure_ascii=False, indent=0), encoding="utf-8")
print(f"pegadinhas geradas acumuladas: {len(peg)}")

# simulados
arq_sim = MAT / "simulados_marcas.json"
marcas = json.loads(arq_sim.read_text(encoding="utf-8")) if arq_sim.exists() else {}
for f in sorted((SCR / "out").glob("*.json")):
    if not valido(SCR / "validar.py", f.stem):
        print(f"simulados: lote {f.stem} reprovado no validador, ficou de fora")
        continue
    for q in json.loads(f.read_text(encoding="utf-8")):
        marcas.setdefault(str(q["sim"]), {})[str(q["n"])] = {"alts": q.get("alts") or {}, "esquema": q["esquema"], "pede": q.get("pede", "correta")}
arq_sim.write_text(json.dumps(marcas, ensure_ascii=False), encoding="utf-8")
n = sum(len(v) for v in marcas.values())
js = RAIZ / "discursiva" / "olho_aguia_simulados.js"
js.write_text("/* GERADO por ferramentas/olho_de_aguia/juntar.py — NÃO edite à mão e NÃO suba ao Git (deriva dos Simulados Delta, D-017). */\n"
              "window.OLHO_SIM=" + json.dumps(marcas, ensure_ascii=False) + ";\n", encoding="utf-8")
print(f"simulados com marcação: {n} questões")

subprocess.run(["node", str(RAIZ / "ferramentas" / "olho_de_aguia" / "montar_assertivas.cjs")], check=True)
