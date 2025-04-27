print("LOJA GORDÃO FOGUETES")

ListCode = [1, 2, 3, 4, 5, 6]
ListFood = ["Hot-dog", "X-Salada", "X-Egg", "X-Tudo", "Refrigerante", "Água"]
ListPrices = [25.00, 30.00, 35.00, 50.00, 08.00, 05.00]

ListCode2 = [1, 2, 3 , 4]
ListDessert = ["Brigadeiro", "Pudim (Pedaço)", "Mousse de Maracujá", "Gelatina"]
ListPrices2 = [1.50, 5.00, 4.50, 2.50]

Confirm = input("Deseja fazer um pedido (S/N)?\n")

if ((Confirm == "S") or (Confirm == "s")):
    
    print("\n")

    Name = input("Digite o seu nome, por favor: ")

    print("\n")

    print(ListCode[0], " - ", ListFood[0], " - " "R$ ", ListPrices[0])                       
    print(ListCode[1], " - ", ListFood[1], " - " "R$ ", ListPrices[1])               
    print(ListCode[2], " - ", ListFood[2], " - " "R$ ", ListPrices[2])   
    print(ListCode[3], " - ", ListFood[3], " - " "R$ ", ListPrices[3])
    print(ListCode[4], " - ", ListFood[4], " - " "R$ ", ListPrices[4])
    print(ListCode[5], " - ", ListFood[5], " - " "R$ ", ListPrices[5])

    Order = int(input("Escolha a opção de desejada: \n"))

    if Order == 1:
        Pedido = 0
    elif Order == 2:
        Pedido = 1
    elif Order == 3:
        Pedido = 2
    elif Order == 4:
        Pedido = 3
    elif Order == 5:
        Pedido = 4
    elif Order == 6:
        Pedido = 5
    else:
        print("Opção inválida, por favor, escolha um número do cardápio")

    qtd = int(input("Digite a quantidade que vocês deseja: \n"))

    Total = qtd * ListPrices[Pedido]

    ped = [Name, ListCode[Pedido], ListFood[Pedido], "R$: ", ListPrices[Pedido], qtd, "R$: ", Total]

    print("\n\n")

    Dessert = input(f"O valor total da compra será de R$: {Total}, deseja alguma sobremesa? (S/N)")

    if ((Dessert == "S") or (Dessert == "s")):
    
        print("\n")

        print(ListCode2[0], " - ", ListDessert[0], " - " "R$ ", ListPrices2[0])                       
        print(ListCode2[1], " - ", ListDessert[1], " - " "R$ ", ListPrices2[1])               
        print(ListCode2[2], " - ", ListDessert[2], " - " "R$ ", ListPrices2[2])   
        print(ListCode2[3], " - ", ListDessert[3], " - " "R$ ", ListPrices2[3])

        print("\n")

        Order2 = input("Escolha uma das opções acima, por favor: ")

else:
    print("Tenha um bom dia!\n")