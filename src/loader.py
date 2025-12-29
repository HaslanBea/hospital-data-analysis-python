# Leitura do Csv loader

import csv

def carregar_atendimentos():
    with open("data/raw/encounters.csv") as f:
        f.readline() # Aqui vai pular a linha do cabeçalho
        atendimentos = [] #Uma lista que vai receber os dados
        for linha in f: # vai ler as linhas
            atendimentos.append(linha.split())
    return atendimentos

