from loader import carregar_atendimentos
from services import contar_atendimentos
from services import calcular_diferenca_custo
from services import tipos_atendimentos
from services import top_providers
from services import media_atendimentos

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
    media = media_atendimentos(atendimentos)
    print(f"Média de duração dos atendimentos: {media}")


if __name__ == "__main__":
    main()

# Regras de negócios foram movidas para services.py
