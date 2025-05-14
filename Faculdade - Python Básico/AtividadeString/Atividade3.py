print("Exercícios - String")

print("3)Elaborar um programa que receba uma palavra ou texto e a imprima de trás-para-frente.")

palavra = []

pal = str(input("digite uma palvra: \n"))

tamanho = len(pal)

y = 0

for n in range (tamanho):
    letra = pal[y]
    palavra.append(letra)
    y = y + 1

print(palavra)