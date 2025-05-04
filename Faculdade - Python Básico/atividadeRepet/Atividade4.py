print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("4)Elaborar um algoritmo que lê 20 números inteiros. Para cada número inserido exibir se é par ou ímpar\\n")

for n in range (20):
    n1 = int(input("Digite um número e te direi se é par ou ímpar\n"))
    if n1 % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")