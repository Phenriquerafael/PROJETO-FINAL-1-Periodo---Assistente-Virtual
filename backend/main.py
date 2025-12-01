from assistente import operacao_matematica, jogo_adivinha, informacoes, conversor

def cabecalho():
    print("=" * 45)
    print("ASSISTENTE VIRTUAL - PROJETO FINAL")
    print("AIB 2025/2026 | Grupo: [Nomes]")
    print("=" * 45)
    print()

def menu():
    print("1 - Operação Matemática")
    print("2 - Jogo Adivinhar o Número")
    print("3 - Informações")
    print("4 - Conversor de Unidades")
    print("5 - Sair")

    while True:
        try:
            op = int(input("Opção: "))
            if 1 <= op <= 5:
                return op
            else:
                print("Escolhe um número entre 1 e 5.")
        except:
            print("Escreve um número válido.")

def main():
    cabecalho()

    nome = input("Como te chamas? ")
    print("Olá,", nome + "!\n")

    ativo = True
    while ativo:
        opcao = menu()

        if opcao == 1:
            operacao_matematica()
        elif opcao == 2:
            jogo_adivinha()
        elif opcao == 3:
            informacoes()
        elif opcao == 4:
            conversor()
        elif opcao == 5:
            print("\nObrigado por usar o Assistente!")
            ativo = False

if __name__ == "__main__":
    main()
