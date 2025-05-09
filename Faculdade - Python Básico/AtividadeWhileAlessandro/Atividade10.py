print("Exercícios - Repetição com while (Pyhton)\n")

print("10) Elaborar um programa que contém uma lista com 15 elementos. Essa lista deve ser preenchida pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista \n")

unique_list = []

normal_list = []

while len(unique_list) < 15:
    num = float(input("Digite um número, se for repetido não será contado"))
    normal_list.append(num)

    unique = set(normal_list)

    if len(unique) == 15:
        unique_list.append(unique)
        break

print(unique_list)