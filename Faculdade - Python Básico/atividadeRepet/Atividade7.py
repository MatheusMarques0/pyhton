print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("7)Elaborar um algoritmo que leia 10 números. Logo após, deve exibir o menor valor lido e o maior valor lido")

numeros = []

for n in range (10):
    num = float(input("Digite um número: \n"))
    numeros.append(num)


menor = min(numeros)
maior = max(numeros)
print("o menor valor é %d e o maior valor é %d" % (menor, maior))