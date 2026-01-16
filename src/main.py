from loader import carregar_atendimentos
from services import contar_atendimentos
from services import calcular_diferenca_custo
from services import tipos_atendimentos
from services import top_providers
from services import media_duracao_atendimentos
from services import media_cobertura_convenio
from services import valor_maximo_atendimento

def main():
    atendimentos = carregar_atendimentos()
    total = contar_atendimentos(atendimentos)
    print(f"Total de atendimentos: {total}")
    diferencas = calcular_diferenca_custo(atendimentos)
    print(f"Diferenças de custo: {diferencas}")
    tipos = tipos_atendimentos(atendimentos)
    print(f"Tipos de atendimentos: {tipos}")
    top = top_providers(atendimentos)
    print(f"Top providers: {top}")
    media = media_duracao_atendimentos(atendimentos)
    print(f"Média de duração dos atendimentos: {media}")
    cobertura = media_cobertura_convenio(atendimentos)
    print(f"A media que o convenio cobriu foi de: {cobertura}")
    maximo = valor_maximo_atendimento(atendimentos)
    print(f"Maior valor de atendimento: {maximo}")



if __name__ == "__main__":
    main()

# Regras de negócios foram movidas para services.py
