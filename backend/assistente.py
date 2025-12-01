"""
Módulo do Assistente Virtual
Contém as funções principais do programa
"""

import random
from datetime import date

class AssistenteVirtual:
    """Classe principal do Assistente Virtual"""
    
    def __init__(self, nome_utilizador=""):
        self.nome_utilizador = nome_utilizador
        self.grupo = {
            "alunos": ["[Aluno 1]", "[Aluno 2]", "[Aluno 3]"],
            "turma": "[Turma]",
            "colegio": "[Colégio]",
            "ano_letivo": "2025/2026"
        }
    
    def exibir_informacoes_grupo(self):
        """Exibe informações do grupo"""
        info = f"""
        ========================================
        ASSISTENTE VIRTUAL - PROJETO FINAL
        ========================================
        Ano Letivo: {self.grupo['ano_letivo']}
        Disciplina: Aplicações Informáticas B
        Turma: {self.grupo['turma']}
        Colégio: {self.grupo['colegio']}
        ========================================
        """
        return info

# Outras funções podem ser organizadas aqui de forma modular

"""
Módulo: assistente.py
Contém as funcionalidades do Assistente Virtual
"""

import random
from datetime import date

def operacao_matematica():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        print("\nOperações disponíveis:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")

        operacao = input("\nEscolha a operação (+, -, *, /): ")

        if operacao == "+":
            print(f"\nResultado: {num1 + num2}")
        elif operacao == "-":
            print(f"\nResultado: {num1 - num2}")
        elif operacao == "*":
            print(f"\nResultado: {num1 * num2}")
        elif operacao == "/":
            if num2 == 0:
                print("\nErro: Divisão por zero!")
            else:
                print(f"\nResultado: {num1 / num2}")
        else:
            print("\nOperação inválida!")
    except ValueError:
        print("\nErro: introduza números válidos.")

def jogo_adivinha():
    numero = random.randint(1, 20)
    tentativas = 5

    print("\n--- Adivinhar o Número ---")
    print("O computador escolheu um número entre 1 e 20.")

    for tentativa in range(1, tentativas + 1):
        try:
            palpite = int(input(f"Tentativa {tentativa}: "))

            if palpite < numero:
                print("Muito baixo!")
            elif palpite > numero:
                print("Muito alto!")
            else:
                print(f"\nAcertaste! O número era {numero}.")
                return
        except ValueError:
            print("Insere um número válido.")

    print(f"\nFicaste sem tentativas. O número correto era {numero}.")

def informacoes():
    print("\n--- Informações sobre o Assistente ---")
    print("Projeto Final AIB 2025/2026")
    print("Criado por: [Nomes dos Alunos]")
    print("Funcionalidades:")
    print(" - Operações matemáticas")
    print(" - Jogo do número")
    print(" - Conversor de unidades")
    print(f"Data atual: {date.today().strftime('%d/%m/%Y')}\n")

def conversor():
    print("\n--- Conversor de Unidades ---")
    print("1. cm → m")
    print("2. m → cm")
    print("3. °C → °F")
    print("4. °F → °C")
    print("5. kg → g")
    print("6. g → kg")

    try:
        opcao = int(input("Escolha a conversão: "))
        valor = float(input("Valor a converter: "))

        if opcao == 1:
            r = valor / 100
        elif opcao == 2:
            r = valor * 100
        elif opcao == 3:
            r = (valor * 9/5) + 32
        elif opcao == 4:
            r = (valor - 32) * 5/9
        elif opcao == 5:
            r = valor * 1000
        elif opcao == 6:
            r = valor / 1000
        else:
            print("Opção inválida.")
            return

        print(f"Resultado: {r}")

    except ValueError:
        print("Erro: valor inválido.")
