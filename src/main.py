# Projeto: Analise de Dados Hospitalares
# Objetivo: Ler dados de atendimentos e gerar estatisticas simples
# Fonte dos dados: Synthea (dados sinteticos)
#Ponto de entrada

import csv
from collections import Counter

'''
#Aqui e feito a contagem de quanta linhas existem 
with open ("data/raw/encounters.csv") as f:
    quantidade = 0
    for linha in f :
        quantidade = quantidade + 1
    print(quantidade - 1)
'''
'''
#Aqui vamos acessar a coluna ano
with open("data/raw/encounters.csv", "r") as f:
    f.readline()  # pula cabeçalho

    for linha in f:
        partes = linha.split(",")
        start = partes[1]
        ano = start[:4]
        print(ano)
        break

'''

#Aqui vamos acessar o ano, e contar quantas vezes ele aparece
anos = []
with open("data/raw/encounters.csv", "r") as f:
    f.readline()
    for linha in f:
        partes = linha.strip().split(",")
        start = partes[1]
        anos.append(start[:4])

contagem = Counter(anos)
print(contagem)

