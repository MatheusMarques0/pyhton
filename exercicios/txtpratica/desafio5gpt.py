lista_num = []
lista_superior = []

num = float(input("Digite um número para ser mostrado na tabuada: "))
while num <= 0:
    num = float(input("[EERO] Digite um valor maior que zero: "))

x = 1
valor = 0

for n in range(10):
    valor = num * x
    lista_num.append(valor)
    print(f"{x} x {num} = {valor} \n")
    x = x + 1

total = sum(lista_num)
media = total / 10

y = 0

for n in range(10):
    superior = lista_num[y]
    if superior > media:
        lista_superior.append(superior)
    y = y + 1

total_superiores = len(lista_superior)
z = 0
for n in range(total_superiores):
    print(f"{lista_superior[z]} \n")
    z = z + 1

print(f"A média é {media} e há {total_superiores} números acima desse valor")