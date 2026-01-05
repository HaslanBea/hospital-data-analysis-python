from loader import carregar_atendimentos
from services import contar_atendimentos
from services import calcular_diferenca_custo


def main():
    atendimentos = carregar_atendimentos()
    total = contar_atendimentos(atendimentos)
    print(f"Total de atendimentos: {total}")
    diferencas = calcular_diferenca_custo(atendimentos)
    print(f"Diferenças de custo: {diferencas}")

if __name__ == "__main__":
    main()

# Regras de negócios foram movidas para services.py
