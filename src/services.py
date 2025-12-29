#Regras de negocios

# vai acessar a const atendiemento no loader e contar subtrair uma linha pq e cabeçalho

# mas como vou mexer eu acho que aqui nao vou precisar de "with open" ja posso fazer talvez uma funçao "quantidade" uma logica de for e contagem

import csv
from loader import carregar_atendimentos

def contar_atendimentos(carregar_atendimentos):
    total = 0 
    for i in carregar_atendimentos: 
        total += 1
    return total