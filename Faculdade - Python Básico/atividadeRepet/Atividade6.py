print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("6)Elaborar um algoritmo que o usuário tenha que digitar 10 números inteiros. No final, o programa deve exibir quantos números são múltiplos de 3, quantos números são menores que 45 e maiores que 55, e qual é o menor número entre eles.\n")

numeros = []
men45 = []
mai55 = []
divisivel = []

for n in range (10):

    num = int(input("Por favor, digite um número: \n"))
    numeros.append(num)

    if num % 3 == 0:
        divisivel.append(num)

    if num < 45 :
        men45.append(num)

    if num > 55:
        mai55.append(num)

menor = min(numeros)
div = len(divisivel)
menor45 = len(men45)
maior55 = len(mai55)

print("No total, existem %d números múltiplos de 3, %d menores que 45, %d maiortes que 55, e o menor número é %d." %(div, menor45, maior55, menor))