from assistente import operacao_matematica, jogo_adivinha, informacoes, conversor

def cabecalho():
    print("=" * 50)
    print("ASSISTENTE VIRTUAL - PROJETO FINAL")
    print("Ano Letivo 2025/2026 | Aplicações Informáticas B")
    print("Grupo: [Nomes] | Turma: [X] | Colégio: [Nome]")
    print("=" * 50)

def menu():
    print("\n1. Operação Matemática")
    print("2. Jogo Adivinhar o Número")
    print("3. Informações")
    print("4. Conversor de Unidades")
    print("5. Sair")

    while True:
        try:
            op = int(input("\nEscolha uma opção: "))
            if 1 <= op <= 5:
                return op
            else:
                print("Escolhe entre 1 e 5.")
        except ValueError:
            print("Insere um número válido.")

def main():
    cabecalho()

    nome = input("Qual é o teu nome? ")
    print(f"Olá, {nome}!\n")

    while True:
        op = menu()

        if op == 1:
            operacao_matematica()
        elif op == 2:
            jogo_adivinha()
        elif op == 3:
            informacoes()
        elif op == 4:
            conversor()
        elif op == 5:
            print("\nObrigado por usar o assistente!")
            break

if __name__ == "__main__":
    main()
