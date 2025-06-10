print("Loja Serjão foguetes")

list_code = [1, 2, 3, 4, 5, 6]
list_desc = ["hot-dog", "X-salada", "X-Egg", "X-Tudo", "refrigerante", "água"]
list_price = [25.00, 30.00, 35.00, 50.00, 08.00, 05.00]

list_code2 = [1, 2, 3, 4]
list_desc2 = ["Brigadeiro", "Pudim", "moussie demaracujá", "gelatina"]
list_price2 = [1.50, 5.00, 4.50, 2.50]

def pedido():
    print("A opção desejada foi de faer um pedido")
    name = str(input("Digite o seu nome: ")).strip()
    while name == " ":
        name = str(input("[ERRO] Não deixe o nome vazio: ")).strip()
    print(f"{list_code[0]}" + " - " + list_desc[0] + " - " + "R$: " + f"{list_price[0]}" + "\n")
    print(f"{list_code[1]}" + " - " + list_desc[1] + " - " + "R$: " + f"{list_price[1]}" + "\n")
    print(f"{list_code[2]}" + " - " + list_desc[2] + " - " + "R$: " + f"{list_price[2]}" + "\n")
    print(f"{list_code[3]}" + " - " + list_desc[3] + " - " + "R$: " + f"{list_price[3]}" + "\n")
    print(f"{list_code[4]}" + " - " + list_desc[4] + " - " + "R$: " + f"{list_price[4]}" + "\n")
    print(f"{list_code[5]}" + " - " + list_desc[5] + " - " + "R$: " + f"{list_price[5]}" + "\n")

    opt = str(input("Esxolha o item desejado: "))
    while opt == "" or (opt != "1" and opt != "2" and opt != "3" and opt != "4" and opt != "5" and opt != "6"):
        opt = str(input("[ERRO] Por favor, digite uma opção válida: "))

    if opt == "1":
        x = 0
    elif opt == "2":
        x = 1
    elif opt == "3":
        x = 2
    elif opt == "4":
        x = 3
    elif opt == "5":
        x = 4
    else:
        x = 5

    qtd = int(input("Digite a quantidade que deseja do produto: "))
    while qtd <= 0:
        qtd = int(input("[ERRO] Digite uma quantidade válida: "))

    total = qtd * list_price[x]
    confirm2 = str(input("O valor da compra de %d unidades de %s será de R$: %0.02F, deseja alguma sobremesa? (1- sim / 2 - mão): " % (qtd, list_desc[x], total)))
    while confirm2 == "" or (confirm2 != "1" and confirm2 != "2"):
        confirm2 = str(input("[ERRO]Por favor escolha uma opção válida (1 = sim / 2 - não): "))
    if confirm2 == "1":
        print(f"{list_code2[0]}" + " - " + list_desc2[0] + " - " + "R$: " + f"{list_price2[0]}" + "\n")
        print(f"{list_code2[1]}" + " - " + list_desc2[1] + " - " + "R$: " + f"{list_price2[1]}" + "\n")
        print(f"{list_code2[2]}" + " - " + list_desc2[2] + " - " + "R$: " + f"{list_price2[2]}" + "\n")
        print(f"{list_code2[3]}" + " - " + list_desc2[3] + " - " + "R$: " + f"{list_price2[3]}" + "\n")

        opt2 = str(input("Escolha o número do item que deseja: "))
        while opt2 == "" or (opt2 != "1" and opt2 != "2" and opt2 != "3" and opt2 != "4"):
            opt2 = str(input("[ERRO] Digite uma opção válida: "))
    
        if opt2 == "1":
            x = 0
        elif opt2 == "2":
            x = 1
        elif opt2 == "3":
            x = 2
        else:
            x = 3

        qtd2 = int(input("Digite a quantidade que deseja do produto: "))
        while qtd2 <= 0:
            qtd2 = int(input("[ERRO] Por favor, digite uma opção maior que 0: "))
        total2 = qtd2 * list_price[x]
        totalfinal = total + total2
        print("o cliente %s comprou %d unidade(s) de %s, com o acompanhamento de %d unidades de %s, dando um total de: %0.2f." %(name, qtd, list_desc[x], qtd2, list_desc2[x], totalfinal))
    else:
        print("Compra cancelada!")

#Main
confirm = str(input("Você deseja fazer um pedido? (1 - sim / 2 - não): "))
while confirm == "" or (confirm != "1" and confirm != "2"):
    confirm = str(input("[ERRO] Digite uma opção válida (1 / 2): "))
if confirm == "1":
    pedido()
else:
    print("A opção desejada foi de não fazer pedidos")