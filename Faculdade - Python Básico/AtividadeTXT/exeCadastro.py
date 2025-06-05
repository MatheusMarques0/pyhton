print("Faça um cadastro de ADM e Operador:")
 
#variáveis
 
confirmar = "s"
confirm = "s"
codigo = 0 #"Boas práticas"
option = 0
optionAdm = 0
description = 0
price = 0
temp = []
dados_temp = []
temp_cod = []
lista_produto = [] # função listar, 87 [codígos]
codigo_produto = [] # código dos pedidos, função listar
 
lista_pedido = [] # lista de pedidos do cliente, será usado em um segundo txt

totalprice = [] #lista que armazenará os preços dos produtos comprados(já multiplicado pela quantia desejada) será usado para dizer o preço total da compra
 
#funções
 
def menu(): #Menu, ele será a primeira coisa a ser chamada, retorna um input
    print("1) ADM")
    print("2) Operador")
    print("3) Sair \n")
 
    option = str(input("Digite qual opção deseja (escreva um número de 1 a 3): ")).strip()
    while option == "" or (option != "1" and option != "2" and option != "3"): #tirando erros
        option = str(input("Por favor, digite um número correto (de 1 a 3): "))
 
    return option
 
def menuADM():
    print("1) Cadastrar")
    print("2) Listar")
    print("3) Editar")
    print("4) Excluir")
    print("5) Sair \n")
 
    optionAdm = str(input("Digite qual opção deseja (escreva um número de 1 a 5): "))
    while optionAdm == "" or (optionAdm != "1" and optionAdm != "2" and optionAdm != "3" and optionAdm != "4" and optionAdm != "5"):
        optionAdm = str(input("Por favor, digite um número correto (de 1 a 5): "))
 
    return optionAdm
 
def CadastrarADM():
 
    temp.clear()
    temp_cod.clear()
   
    print("\nA opção desejada foi de cadastrar no modo ADM")
    codigo = 0
    arquivo = open("cadastroADM.txt", 'r', encoding='utf-8')
    dados = arquivo.readlines()
 
    if dados == []:
        codigo = 100
        print("teste")
        arquivo.close()
    else:
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')
            dados[i] = dados[i].split(';')
            temp.append(dados[i][0])
        arquivo.close()
 
        for p in range(len(temp)):
            temp[p] = int(temp[p])  
        numeros = set(temp)
        esperado = set(range((100), max(numeros) + 1))
        faltantes = sorted(esperado - set(numeros))
        if faltantes == []:
            codigo = str(max(temp) + 1)
        else:
            for numero in faltantes:
                temp_cod.append(numero)
            codigo = str(temp_cod[0])
 
    print(f"Código do produto: {codigo}")
 
    description = str(input("Descreva o arquivo a ser computado: "))
    while (description == ""):
        print("Valor inválido \n")
        description = str(input("Descreva o arquivo a ser computado: "))
 
    price = str(input("Digite qual será o preço do produto: "))
    while (price == "" or price.isalpha()):
        print("Valor inválido! \n")
        price = str(input("Digite qual será o preço do produto: "))
 
    arquivo = open("cadastroADM.txt", 'a+', encoding='utf-8')
    if dados == []:
        arquivo.write(f"{codigo}" + ";" + description + ";" + price)
        arquivo.close()
    else:
        dados.append([codigo, description, price])
        lista_cad = sorted(dados, key=lambda x: int(x[0]))
        arquivo = open("cadastroADM.txt", "w", encoding='utf-8')
        for g in range (len(lista_cad)):
            arquivo.write(str(lista_cad[g][0]) + ";" + str(lista_cad[g][1]) + ";" + str(lista_cad[g][2]) + "\n")
        arquivo.close()
 
    print("Arquivo gerado com sucesso!")
 
def ListarADM():
    codigo_produto.clear() #isso é para limpar a lista, sem isso a lista ficará
    lista_produto.clear() #. clear limpa completamente a lista em python, anota, anota, anota
    arquivo = open("cadastroADM.txt", "r", encoding ='utf-8')
    listar = arquivo.readlines()
    for n in range(len(listar)):
        listar[n] = listar[n].strip('\n') #transformando linnhas do txt em listas, sem espaçoes e sem dividas pelos ";"
        listar[n] = listar[n].split(';')
        codigo_produto.append(listar[n][0])
        lista_produto.append(listar[n])
        print(listar[n])
    arquivo.close()
    print("\n")
 
def EditarADM():
    ListarADM() #chamando a função, reduzindo código
 
    arquivo = open("cadastroADM.txt", "r", encoding='utf-8')
 
    print("A opção desejada foi Editar como ADM\n")
         
    cod_alterar = str(input("Digite o código do produto que deseja alterar: "))
    while cod_alterar not in codigo_produto:
        cod_alterar = str(input("[ERRO], por favor digite um código que exista: "))
 
    codigo_changer = codigo_produto.index(cod_alterar)
    print("\nA descrição atual do produto é: %s" %(lista_produto[codigo_changer][1])) #amém, eu tive que criar 2 listas para que ess método funcionasse, uma com os código e uma com os pedidos
 
    new_description = str(input("Digite a nova descrição do produto: "))
    while (new_description == ""):
        new_description = str(input("[ERRO] Não deixe o espaço vazio, digite uma opção válida: "))
 
    print("\nO preço atual do produto é: %s" %(lista_produto[codigo_changer][2]))
 
    new_price = str(input("Digite um novo preço para o produto: "))
    while (new_price == ""):
        new_price = str(input("[ERRO] Não deixe o espaço vazio, digite uma opção válida: "))
 
    print("O nova descrição do produto de código %s é: %s" %(codigo_produto[codigo_changer], new_description))
    print("O novo preço de %s é: %s" %(new_description, new_price))
               
    lista_produto[codigo_changer][1] = new_description
    lista_produto[codigo_changer][2] = new_price
 
    arquivo.close()
 
    arquivo = open("cadastroADM.txt", "w", encoding='utf-8')
    for n in range(len(lista_produto)):
        arquivo.write(lista_produto[n][0] + ";" + lista_produto[n][1] + ";" + lista_produto[n][2] + "\n")
    arquivo.close()
 
def ExcluirADM():
    ListarADM() #chamando a função, reduzindo código
 
    print("A opção desejada foi de Excluir como ADM\n")
         
    cod_erase = str(input("Digite o código do produto que deseja excluir: "))
    while cod_erase not in codigo_produto:
        cod_erase = str(input("[ERRO], por favor digite um código que exista: "))
 
    codigo_changer = codigo_produto.index(cod_erase)
    print("\nO produto selecionado tem o código: %s. Descrição: %s. Preço: %s \n" %(lista_produto[codigo_changer][0], lista_produto[codigo_changer][1], lista_produto[codigo_changer][2]))
 
    conf = str(input("Tem certeza que deseja apagar o produto? (1 = 'sim' / 2 = 'não'): "))
    while (conf != "1" and conf != "2"):
        conf = str(input("[ERRO] por favor digite uma opçã válida (1 ou 2): "))
 
    if conf == "1":
        lista_produto.pop(codigo_changer)
        codigo_produto.pop(codigo_changer)
 
        with open("cadastroADM.txt", "w", encoding="utf-8") as arquivo: #se não colocar "with open" o 'arquivo' da erro
            for n in range(len(lista_produto)):
                arquivo.write(lista_produto[n][0] + ";" + lista_produto[n][1] + ";" + lista_produto[n][2] + "\n")

        print("\n")

        print("Produto cancelado com sucesso!\n")
    else:
        print("Ação Cancelada! \n")
 
 
def operator():
    totalprice.clear() # se ele for em cancelar novas requições, quer dizer que ele não que mais comprar, por isso resetará essa lista
    choise = 1
 
    name = str(input("Digite o seu nome: "))
    while name == "":
        name = str(input("[ERRO] Digite um nome válido: "))
 
    while choise == 1:
        lista_pedido.clear() # se ele quiser continuar a compra, a lista de pedidos será resetada, porém o preço ficará na lista totalprice (linha 20)
        ListarADM()
        choose = str(input("Digite o código do produto que deseja comprar: "))
        while choose not in codigo_produto:
            choose = str(input("[ERRO] por favor digite um número válido: "))
 
        codigo_choosed = codigo_produto.index(choose)
        print("\nO produto selecionado tem o código: %s. Descrição: %s. Preço: %s \n" %(lista_produto[codigo_choosed][0], lista_produto[codigo_choosed][1], lista_produto[codigo_choosed][2]))#Como é bom reaproveitar código...Quero só ver na prova :D
 
        quantidade = int(input("Digite a quantidade que deseja do produto: "))
        while quantidade <= 0:
            quantidade = int(input("[EROO] Digite uma quantidade VÁLIDA para o produto: "))
 
        realmoney = float(lista_produto[codigo_choosed][2])
 
        despesa = realmoney * quantidade
 
        print("O total será de %0.2f \n" % (despesa))
 
        print("Pedido do Cliente %s: Código: %s.  Descrição: %s. Preço: %s. Quantidade Unitária: %d Total a pagar: %0.2f \n" %(name, lista_produto[codigo_choosed][0], lista_produto[codigo_choosed][1], lista_produto[codigo_choosed][2], quantidade, despesa))
 
        conf = str(input("Deseja confirmar o pedido? (1 = sim / 2 = não): "))
        while (conf != "1" and conf != "2"):
            conf = int(input("[ERRO] Digite um comando válido (1/2): "))
 
        if conf == "1":
            print("Pedido Enviado com sucesso!")
            lista_pedido.append([name, lista_produto[codigo_choosed][0], lista_produto[codigo_choosed][1], lista_produto[codigo_choosed][2], f"{despesa}"])
            totalprice.append(despesa)
 
            arquivo = open("pedidos.txt", 'a+',  encoding='utf-8')
            dados = arquivo.readlines()
 
            if dados == []:
                arquivo.write((lista_pedido[0][0]) + ": " + (lista_pedido[0][1]) + " " + (lista_pedido[0][2]) + " " + (lista_pedido[0][3]) + " " + (lista_pedido[0][4]) + "\n")
                arquivo.close()
            else:
                for i in range(len(dados)):
                    arquivo.write((lista_pedido[0][0]) + ": " + (lista_pedido[0][1]) + " " + (lista_pedido[0][2]) + " " + (lista_pedido[0][3]) + " " + (lista_pedido[0][4]) + "\n")
                arquivo.close()
 
 
        else:
            print("Pedido cancelado!")
 
        repeat = str(input("Deseja reenviar outro pedido? (1 = sim / 2 = não): "))
        while repeat != "1" and  repeat != "2":
            repeat = str(input("[ERRO] Digite um código válido (1 - sim / 2 - não): "))

        if repeat == "1":
            print("A opção desejada foi de continuar as requisições")
        else:
            print("A opção desejada foi de cancelar mais requisições \n")
            pricebuy = sum(totalprice)
            
            confirpurchase = str(input("O total da compra será de: %s reais, deseja confirmar a compra? (1 = sim / 2 = não): " %(pricebuy)))

            while confirpurchase != "1" and confirpurchase != "2":
                confirpurchase = str(input("[ERRO] Número inválido, digite uma opção correta (1 - sim / 2 - não): "))

            if confirpurchase == "1":
                arquivo = open("pedidos.txt", "a+", encoding='utf-8')
                arquivo.seek(0) #leva o cursor para o início para poder ler

                #if linha == [] é possível aqui? 

                arquivo.write(name + " | Total a pagar: " + str(pricebuy) + " reais")
                arquivo.close()

                print("Compra feita com sucesso!")

            else:
                print("Compra Cancelada!") 

            choise = 2
           
 
    print("\n\n")
 
#Main
 
while confirm == "s":
 
    escolha = menu() # Mostrará o menu principal, e o resultado virará uma variável
 
    if escolha == "1": #Se escolher adm...
        print("A opção desejada foi de entrar como ADM\n")
        while confirmar == "s":
            escolhaAdm = menuADM()
 
            if escolhaAdm == "1": #Escolhas do modo ADM
                CadastrarADM()
            elif escolhaAdm == "2":
                print("\nA opção desejada foi de Listar como ADM\n")
                ListarADM()
            elif escolhaAdm == "3":
                print("A opção deseajda foi de Editar como ADM\n")
                EditarADM()
            elif escolhaAdm == "4":
                print("A opção desejada foi de Excluir como ADM\n")
                ExcluirADM()
            elif escolhaAdm == "5":
                print("A opção desejada foi de sair do modo ADM\n")
                break
            else:
                print("[ERRO] digite um número válido (1 a 5): ")
 
    elif escolha == "2": #Se escolher operador... #se for 2, modo Operador
        print("A opção desejada foi de entrar como Operador! \n")
        operator()
 
    elif escolha == "3": #Se escolher sair...
        print("A opção desejada foi de sair")
        print("\n")
        confirm = "n"
    else: #Se nenhuma das opções for correta:
        print("[ERRO] Dígito inválido \n")