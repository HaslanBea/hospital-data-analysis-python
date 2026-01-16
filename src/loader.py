# Leitura do Csv loader

import csv
from pathlib import Path

def carregar_atendimentos():
    # Caminho até a pasta src
    base_dir = Path(__file__).resolve().parent

    # Volta para a raiz do projeto e entra em data/raw
    caminho_csv = base_dir.parent / "data" / "raw" / "encounters.csv"

    atendimentos = []

    with open(caminho_csv, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            atendimentos.append(linha)

    return atendimentos


