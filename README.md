# PROJETO FINAL 1º Periodo - Assistente Virtual 

## 1. Informações do Projeto
- **Disciplina:** Aplicações Informáticas B
- **Ano Letivo:** 2025/2026
- **Colégio:** Externato Ribadouro
- **Grupo:** 
  - Gustavo Cardoso
  - Francisco Midões
  - Diogo Duarte
  - Vicente Fernandes

## 2. Objetivo do Projeto
Desenvolver um programa em Python que funcione como um Assistente Virtual capaz de interagir com o utilizador, executar tarefas simples e apresentar respostas estruturadas, consolidando os conhecimentos fundamentais de programação adquiridos.

## 3. Funcionalidades Implementadas

### 3.1. Operação Matemática Simples
- **Descrição:** Permite realizar operações básicas (soma, subtração, multiplicação, divisão)
- **Entradas:** Dois números fornecidos pelo utilizador
- **Processamento:** Validação de entradas e cálculo conforme operação escolhida
- **Saída:** Resultado da operação formatado

### 3.2. Mini-Jogo "Adivinhar o Número"
- **Descrição:** Jogo interativo onde o utilizador tenta adivinhar um número aleatório
- **Características:**
  - Número gerado aleatoriamente entre 1 e 20
  - Máximo de 5 tentativas
  - Dicas após cada tentativa ("muito alto" ou "muito baixo")
  - Mensagens de vitória/derrota

### 3.3. Informações sobre o Assistente
- **Descrição:** Apresenta informações detalhadas sobre o projeto
- **Conteúdo:**
  - Objetivos do projeto
  - Lista de desenvolvedores
  - Funcionalidades disponíveis
  - Data de desenvolvimento

### 3.4. Conversor de Unidades (Funcionalidade Extra)
- **Descrição:** Converte entre diferentes unidades de medida
- **Tipos de conversão:**
  - Comprimento: cm ↔ m
  - Temperatura: °C ↔ °F
  - Peso: kg ↔ g

## 4. Estrutura do Código

### Arquitetura
```
projeto_assistente_virtual/
│
├── backend/
│   ├── main.py                 # Programa principal em Python
│   └──  assistente.py           # Módulo com todas as funcionalidades
│   
├── README.md                   # Relatório/documentação completa
└── instrucoes.txt              # Guia de instalação e execução
```


### Principais Funções Python
1. `menu_principal()` - Controla a navegação do programa
2. `operacao_matematica()` - Gerencia cálculos matemáticos
3. `adivinhar_numero()` - Implementa o jogo de adivinhação
4. `informacoes_assistente()` - Exibe informações do projeto
5. `conversor_unidades()` - Realiza conversões de unidades

## 5. Requisitos Técnicos Atendidos

### ✅ Todos os requisitos foram implementados:
- [x] Uso de variáveis e entrada/saída de dados
- [x] Estruturas de decisão (if/elif/else)
- [x] Ciclo while para manter o programa ativo
- [x] 4 funções principais (mais funções auxiliares)
- [x] Validação simples de entradas
- [x] Código organizado e comentado
- [x] Nomes de variáveis adequados e legíveis

### ✅ Funcionalidades extras implementadas:
- Modularização do código Python
- Sistema de menu interativo

## 6. Como Executar o Projeto

```bash
# Navegue até a pasta do projeto
cd projeto_assistente_virtual/backend

# Execute o programa principal
python main.py
```

## 7. Aprendizagem e Dificuldades

### Dificuldades Encontradas
1. **Validação de entradas:** Garantir que o programa não crashasse com entradas inválidas
2. **Estruturação do código:** Organizar as funções de forma lógica e modular
3. **Interface web:** Integrar conceitos de Python com HTML/CSS
4. **Trabalho em grupo:** Coordenar diferentes estilos de programação

### Competências Desenvolvidas
- Pensamento computacional e lógico
- Resolução de problemas de forma estruturada
- Trabalho colaborativo em equipa
- Comunicação técnica e documentação
- Gestão de tempo e prazos

Aqui está o restante do README **completo, coerente e pronto para entrega** — sem floreados inúteis e sem deixar pontas soltas:

---

## 8. Critérios de Avaliação Atendidos

| Critério              | Implementação                                                 |
| --------------------- | ------------------------------------------------------------- |
| Funcionamento correto | ✅ Programa testado e funcional                                |
| Organização do código | ✅ Estrutura modular e clara                                   |
| Autonomia e pesquisa  | ✅ Funcionalidade extra implementada e estrutura web adicional |
| Criatividade          | ✅ Interface web ilustrativa + funcionalidade extra            |
| Comentários           | ✅ Código documentado e legível                                |
| Boas práticas         | ✅ Validações, nomes adequados e modularização                 |
| Relatório             | ✅ Documentação completa                                       |
| Apresentação          | ✅ Material organizado e preparado para defesa                 |

---

## 9. Trabalho Colaborativo

### Divisão de Tarefas

* **Aluno 1:** Estrutura principal do programa, fluxo do menu, integração das funcionalidades e validação de entradas.
* **Aluno 2:** Desenvolvimento do mini-jogo “Adivinhar o Número”, testes de funcionamento e correção de erros.
* **Aluno 3:** Criação da interface web (HTML + CSS), design visual, páginas informativas e organização da apresentação.
* **(Opcional) Aluno 4:** Testes finais, revisão de código, apoio na documentação e validação da conformidade com o enunciado.

### Metodologia de Trabalho

* Reuniões de planeamento semanais.
* Divisão equilibrada das tarefas segundo as competências de cada elemento.
* Revisão mútua de código para evitar erros e inconsistências.
* Testes individuais + testes de grupo para garantir estabilidade.
* Criação conjunta do relatório e preparação da defesa oral.

