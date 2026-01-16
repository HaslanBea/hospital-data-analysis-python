from datetime import datetime


def contar_atendimentos(atendimentos):
    return len(atendimentos)


def calcular_diferenca_custo(atendimentos):
    sem_acrescimo = 0
    soma = 0
    quantidade = 0

    for atendimento in atendimentos:
        custo_base = float(atendimento["BASE_ENCOUNTER_COST"])
        custo_final = float(atendimento["TOTAL_CLAIM_COST"])

        acrescimo = custo_final - custo_base

        if acrescimo == 0:
            sem_acrescimo += 1
        else:
            soma += acrescimo
            quantidade += 1

    if quantidade == 0:
        return {
            "media_acrescimo": 0,
            "sem_acrescimo": sem_acrescimo
        }

    media = soma / quantidade

    return {
        "media_acrescimo": media,
        "sem_acrescimo": sem_acrescimo
    }


def tipos_atendimentos(atendimentos):
    contagem = {}

    for atendimento in atendimentos:
        tipo = atendimento["ENCOUNTERCLASS"]

        if tipo in contagem:
            contagem[tipo] += 1
        else:
            contagem[tipo] = 1

    return contagem


def atendimentos_por_provider(atendimentos):
    contagem = {}

    for atendimento in atendimentos:
        provider = atendimento["PROVIDER"]

        if provider in contagem:
            contagem[provider] += 1
        else:
            contagem[provider] = 1

    return contagem


def top_providers(atendimentos, limite=3):
    contagem = atendimentos_por_provider(atendimentos)
    return sorted(contagem.items(), key=lambda x: x[1], reverse=True)[:limite]


def media_duracao_atendimentos(atendimentos):
    soma_duracao = 0
    quantidade = 0

    for atendimento in atendimentos:
        inicio = datetime.strptime(atendimento["START"], "%Y-%m-%dT%H:%M:%SZ")
        fim = datetime.strptime(atendimento["STOP"], "%Y-%m-%dT%H:%M:%SZ")

        duracao_horas = (fim - inicio).total_seconds() / 3600

        soma_duracao += duracao_horas
        quantidade += 1

    if quantidade == 0:
        return 0

    return soma_duracao / quantidade

# cobertura média do convênio

def media_cobertura_convenio(atendimentos):
    soma_cobertura = 0
    quantidade = 0

    for atendimento in atendimentos:
        cobertura = float(atendimento["PAYER_COVERAGE"])  # PAYER_COVERAGE
        soma_cobertura += cobertura
        quantidade += 1

    if quantidade > 0:
        return soma_cobertura / quantidade
    else:
        return 0

# Quais foram o atendimento mais caro?

def valor_maximo_atendimento(atendimentos):
    return max(float(atendimento["BASE_ENCOUNTER_COST"]) for atendimento in atendimentos)

