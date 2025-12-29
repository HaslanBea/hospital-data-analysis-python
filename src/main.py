from loader import carregar_atendimentos
from services import contar_atendimentos

def main():
    atendimentos = carregar_atendimentos()
    total = contar_atendimentos(atendimentos)
    print(f"Total de atendimentos: {total}")

if __name__ == "__main__":
    main()
