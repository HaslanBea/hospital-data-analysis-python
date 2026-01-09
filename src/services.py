import csv
from loader import carregar_atendimentos
from datetime import datetime



lista_atendimentos = carregar_atendimentos()

def contar_atendimentos(carregar_atendimentos):
    total = 0 
    for i in carregar_atendimentos: 
        total += 1
    return total


#  Diferença entre custo base e custo final?
def calcular_diferenca_custo(atendimentos):
    sem_acrescimo = 0
    soma = 0
    quantidade = 0

    for atendimento in atendimentos:
        custo_base = float(atendimento[10]) 
        custo_final = float(atendimento[11]) 
        acrescimo = custo_final - custo_base

        if acrescimo == 0:
            sem_acrescimo += 1
        else:
            soma += acrescimo
            quantidade += 1

    if quantidade == 0:
        print("Não existe atendimento com acréscimo")
    else:
        media = soma / quantidade
        print(f"Média dos acréscimos: {media}")

    print(f"Total de atendimentos sem acréscimo: {sem_acrescimo}")


def tipos_atendimentos(atendimentos):
    contagem = {}

    for atendimento in atendimentos:
        tipo = atendimento[7]  # ENCOUNTERCLASS

        if tipo in contagem:
            contagem[tipo] += 1
        else:
            contagem[tipo] = 1

    return contagem

resultado = tipos_atendimentos(lista_atendimentos)

for tipo, quantidade in resultado.items():
    print(f"{tipo}: {quantidade}")

def atendimentos_por_provider(atendimentos):
    contagem = {}

    for atendimento in atendimentos:
        provider = atendimento[5]

        if provider in contagem:
            contagem[provider] += 1
        else:
            contagem[provider] = 1

    return contagem


def top_providers(atendimentos):
    contagem = atendimentos_por_provider(atendimentos)
    top_5 = sorted(contagem.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_5

def media_atendimentos(atendimentos):
    soma_duracao = 0
    quantidade = 0

    for atendimento in atendimentos:
        inicio_str = atendimento[1]  # START
        fim_str = atendimento[2]     # STOP

        inicio = datetime.strptime(inicio_str, "%Y-%m-%dT%H:%M:%SZ")
        fim = datetime.strptime(fim_str, "%Y-%m-%dT%H:%M:%SZ")

        duracao = (fim - inicio).total_seconds() / 3600  # duração em horas

        soma_duracao += duracao
        quantidade += 1

    if quantidade == 0:
        print("Não há atendimentos para calcular a média.")
        return 0

    media = soma_duracao / quantidade
    print(f"Média de duração dos atendimentos (em horas): {media}")
    return media
