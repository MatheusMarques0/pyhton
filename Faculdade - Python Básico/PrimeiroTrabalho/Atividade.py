print("1°Trabalho Avaliativo \n")

pessoas = [1, 2, 3, 4, 5, 6]
dia1 = [20, 28, 35, 42, 48, 53]
dia2 = [25, 34, 42, 50, 57, 63]

print("quantidade de pessoas - Tipo 1 | Tipo 2 \n")

print(pessoas[0], " - " " R$: ", dia1[0], " R$: ", dia2[0])
print(pessoas[1], " - " " R$: ", dia1[1], " R$: ", dia2[1])
print(pessoas[2], " - " " R$: ", dia1[2], " R$: ", dia2[2])
print(pessoas[3], " - " " R$: ", dia1[3], " R$: ", dia2[3])
print(pessoas[4], " - " " R$: ", dia1[4], " R$: ", dia2[4])
print(pessoas[5], " - " " R$: ", dia1[5], " R$: ", dia2[5])

print("\n")

qtd = int(input("Bem vindo, digite quantas pessoas ocuparão o apartamento (limite de 6 pessoas): \n"))

while qtd > 6 or qtd < 1:
    qtd = int(input("Número inválido, digite um número entre 1 e 6: \n"))

if qtd == 1:
    x = 0
elif qtd == 2:
    x = 1
elif qtd == 3:
    x = 2
elif qtd == 4:
    x = 3
elif qtd == 5:
    x = 4
else:
    x = 5

print("Para uma quantidade de %d pessoas, nossos preços são: \n" % (qtd))

print("Tipo 1", " - ", "R$:", dia1[x])
print("Tipo 2", " - ", "R$:", dia2[x])

print("\n")

tipo = int(input("Digite o seu tipo de apartamento (1 ou 2): \n"))

while tipo < 1 or tipo > 2:
    tipo = int(input("Número inválido, digite um número entre 1 e 2: \n"))

if tipo == 1:
    print(f"O valor a ser pago, por um apartamento de Tipo 1, com {pessoas[x]} pessoas, será de R$:", dia1[x])
else:
    print(f"O valor a ser pago, por um apartamento de Tipo 2, com {pessoas[x]} pessoas, será de R$:", dia2[x])