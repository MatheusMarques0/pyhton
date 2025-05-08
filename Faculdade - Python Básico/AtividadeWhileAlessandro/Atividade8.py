print("Exercícios - Repetição com while (Pyhton)\n")

print("8) Elaborar um programa que contém uma lista com N elementos. Essa lista deve ser preenchida pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o número 1 a repetição termina. Exibir no final todos os elementos da lista. \n")

lista = []

num = int(input("Digite um número positivo e par para adicionar à lista \n"))


while (num != 1):
    if (num % 2 == 0 and num > 0):
        lista.append(num)
        num = int(input("Digite outro número para adicionar á lista, digite 1 para finalizar a requisição. \n"))

    else:
        num = int(input("Número não se encaixa nos parâmetros acima, não computado na lista. Adicione outro número: \n"))

else:
    print(lista)
    print('Fim do programa')
    