print("Exercícios - Repetição com while (Pyhton)\n")

print("10) Elaborar um programa que contém uma lista com 15 elementos. Essa lista deve ser preenchida pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista \n")

unique_list = []

while len(unique_list) < 15:
    entrada = input("Digite um número (números repetidos não serão computados): ")

    i = 0
    e_valido = 1
    while i < len(entrada):
        c = entrada[i]
        if not (c.isdigit() or c == '.' or (i == 0 and c == '-')):
            e_valido = 0
        i += 1

    if e_valido == 0:
        print("Entrada inválida. Por favor, digite um número.")
    else:
        num = float(entrada)

        i = 0
        repetido = 0 
        while i < len(unique_list):
            if unique_list[i] == num:
                repetido = 1
            i += 1

        if repetido == 1:
            print("Número repetido! Tente outro.")
        else:
            unique_list.append(num)

print("\nLista final com 15 números únicos:")
print(unique_list)

