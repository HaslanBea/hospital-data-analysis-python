import csv
from loader import carregar_atendimentos

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

