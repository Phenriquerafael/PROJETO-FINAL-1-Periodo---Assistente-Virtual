import random
from datetime import date

def operacao_matematica():
    print("\n--- Operação Matemática ---")

    try:
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))
    except:
        print("Erro: tens de escrever números.")
        return

    print("\nEscolhe a operação:")
    print("+  Soma")
    print("-  Subtração")
    print("*  Multiplicação")
    print("/  Divisão")

    op = input("Operação: ")

    if op == "+":
        print("Resultado:", n1 + n2)
    elif op == "-":
        print("Resultado:", n1 - n2)
    elif op == "*":
        print("Resultado:", n1 * n2)
    elif op == "/":
        if n2 == 0:
            print("Não dá para dividir por zero.")
        else:
            print("Resultado:", n1 / n2)
    else:
        print("Operação inválida.")

def jogo_adivinha():
    print("\n--- Adivinhar o Número ---")
    numero = random.randint(1, 20)
    tentativas = 5

    for i in range(1, tentativas + 1):
        try:
            palpite = int(input("Tentativa " + str(i) + ": "))
        except:
            print("Escreve um número.")
            continue

        if palpite < numero:
            print("Muito baixo.")
        elif palpite > numero:
            print("Muito alto.")
        else:
            print("Acertaste! O número era", numero)
            return

    print("Ficaste sem tentativas. O número era", numero)

def informacoes():
    print("\n--- Informações ---")
    print("Projeto Final - Assistente Virtual")
    print("Ano Letivo: 2025/2026")
    print("Colégio: Externato Ribadouro")
    print("Autores:")
    print(" - Gustavo Cardoso")
    print(" - Francisco Midões")
    print(" - Diogo Duarte")
    print(" - Vicente Fernandes")
    print()
    print("Funcionalidades:")
    print("- Operações matemáticas")
    print("- Jogo de adivinhar o número")
    print("- Conversor de unidades")
    print("Data:", date.today().strftime("%d/%m/%Y"))
    print("---------------------------")
    print()

def conversor():
    print("\n--- Conversor de Unidades ---")
    print("1. cm → m")
    print("2. m → cm")
    print("3. °C → °F")
    print("4. °F → °C")
    print("5. kg → g")
    print("6. g → kg")

    try:
        op = int(input("Escolha a opção: "))
        valor = float(input("Valor: "))
    except:
        print("Erro: valor inválido.")
        return

    if op == 1:
        print("Resultado:", valor / 100)
    elif op == 2:
        print("Resultado:", valor * 100)
    elif op == 3:
        print("Resultado:", (valor * 9/5) + 32)
    elif op == 4:
        print("Resultado:", (valor - 32) * 5/9)
    elif op == 5:
        print("Resultado:", valor * 1000)
    elif op == 6:
        print("Resultado:", valor / 1000)
    else:
        print("Opção inválida.")
