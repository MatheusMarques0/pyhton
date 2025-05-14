print("Exercícios - String")

print("1)Elaborar um programa que leia um nome e imprima as 4 primeiras letras do nome\n")

nome = str(input("Digite um nome (com quatro letras ou mais): \n"))

caprichos = len(nome)

while caprichos < 4:
    nome = str(input("Palavra com menos de quatro caracteres, digite um nome (com quatro letras ou mais): \n"))
    caprichos = len(nome)
else:

    um = nome[0]
    dois = nome[1]
    tres = nome[2]
    quatro = nome[3]

    print("%s%s%s%s" % (um, dois, tres, quatro))