print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("8)Elaborar um algoritmo que some todos os números inteiros abaixo de 1000 que são múltiplos de 3 ou 5\n")

divisivel = []
EspecificoDeMais = []

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        divisivel.append(n)

soma = sum(divisivel)

print("A soma dos números deu %d" % (soma))