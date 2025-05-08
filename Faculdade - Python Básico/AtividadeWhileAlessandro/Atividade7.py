print("Exercícios - Repetição com while (Pyhton)\n")

print("Elaborar um programa para automatizar o caixa de uma lanchonete. Este programa deve ler o código do item  pedido, a quantidade e somar para calcular o valor a ser pago. O programa termina quando o código for 0(zero). O cardápio da lanchonete é o seguinte: \n")

cod = [100, 101, 102, 103, 104, 105]
esp = ["Cachorro quente", "Bauru simples", "Bauru c/ovo", "Hamburger", "Cheeseburger", "Refrigerante"]
price =  [3.50, 3.80, 4.50, 4.70, 5.30, 4.00]

print(cod[0], " - ", esp[0], " - ", "R$ ", price[0])
print(cod[1], " - ", esp[1], " - ", "R$ ", price[1])
print(cod[2], " - ", esp[2], " - ", "R$ ", price[2])
print(cod[3], " - ", esp[3], " - ", "R$ ", price[3])
print(cod[4], " - ", esp[4], " - ", "R$ ", price[4])
print(cod[5], " - ", esp[5], " - ", "R$ ", price[5])

pd = int(input("Digite o seu pedido:\n"))

while (pd != 0):

    while (pd < 100 or pd > 105):
        pd = int(input("Número incorreto, por favor digite um número da lista: \n"))

    if pd == 100:
        x = 0
    elif pd == 101:
        x = 1
    elif pd == 102:
        x = 2
    elif pd == 103:
        x = 3
    elif pd == 104:
        x = 4
    else: 
        pd == 105
        x = 5

    qtd = int(input("Escolha a quantidade desejada:\n"))

    total = qtd * price[x]

    pedido = [cod[x], esp[x], total]

    print(pedido)

    print("\n")

    print("O código do pedido é %d, %s. Quantidade solicitada: %d, total a se pagar R$: %0.2f" % (cod[x], esp[x], qtd, total))

    print(cod[0], " - ", esp[0], " - ", "R$ ", price[0])
    print(cod[1], " - ", esp[1], " - ", "R$ ", price[1])
    print(cod[2], " - ", esp[2], " - ", "R$ ", price[2])
    print(cod[3], " - ", esp[3], " - ", "R$ ", price[3])
    print(cod[4], " - ", esp[4], " - ", "R$ ", price[4])
    print(cod[5], " - ", esp[5], " - ", "R$ ", price[5])

    pd = int(input("Deseja fazer outro pedido? Digite 0(zero) para encerrar o programa:\n"))

else:
    print("Solicitação concluída.")