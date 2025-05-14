print("Exercícios - String")

print("2)Elaborar um programa que leia um nome e imprima o nome somente se a primeira letra do nome for 'a' (maiúscula ou minúscula)\n")

nome = str(input("Digite um nome: \n"))

letra1 = nome[0]

if letra1 == "a" or letra1 == "A":
    print(f"{nome}")