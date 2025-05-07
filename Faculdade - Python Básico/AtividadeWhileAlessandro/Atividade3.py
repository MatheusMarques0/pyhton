print("Exercícios - Repetição com while (Pyhton) \n")

print("3) Elaborar um programa que deve ler N números. Caso o usúario digite zero (0), o programa deve exibir a somatória e a média dos valores inseridos. \n")

lista = []

num = float(input("Digite um número: \n"))

while (num != 0):
    lista.append(num)
    num = float(input("Digite outro número: \n"))

else:
    soma = sum(lista)
    print("A somatória das listas é de %0.2f" % (soma))