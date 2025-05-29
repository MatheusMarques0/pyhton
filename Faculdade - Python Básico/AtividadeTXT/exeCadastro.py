print("Faça um cadastro de ADM e Operador:")

#variáveis

confirmar = "s"
confirm = "s"
codigo = 0 #"Boas práticas"
option = 0
optionAdm = 0
description = 0
price = 0
dados = []

lista_produto = [] # função listar, 87 [codígos]
codigo_produto = [] #código dos pedidos, função listar

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
    temp = []
    temp_cod = []

    print("\nA opção desejada foi de cadastrar no modo ADM")
    codigo = 0
    arquivo = open("cadastroADM.txt", 'r', encoding='utf-8')
    dados = arquivo.readlines()
    arquivo.close() # lembrar de perguntar o professor se isso pode fazer
    if dados == []:
        codigo = 100
    else:
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')
            dados[i] = dados[i].split(';')
            temp.append(dados[i][0])
 
        for i in range(len(temp)):
            temp[i] = int(temp[i])  
        numeros = set(temp)
        esperado = set(range(min(numeros), max(numeros) + 1))
        faltantes = sorted(esperado - set(numeros))
        if faltantes == []:
            codigo = str(max(temp) + 1)
        else:
            for numero in faltantes:
                temp_cod.append(numero)
            codigo = str(temp_cod[0])


    print("A opção escolhida foi cadastrar produtos")
    print(f"Código do pedido:{codigo}\n")

    arquivo = open("cadastroADM.txt", "a")
    description = str(input("Descreva o arquivo a ser computado: "))
    price = str(input("Digite qual será o preço do produto: "))
    arquivo.write(f"{codigo};{description};{price}\n")
    arquivo.close()
    print("Arquivo gerado com sucesso!")

def ListarADM():
    codigo_produto.clear() #isso é para limpar a lista, sem isso a lista ficará 
    lista_produto.clear() #. clear limpa completamente a lista em python, anota, anota, anota
    arquivo = open("cadastroADM.txt", "r")
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

    print("A opção desejada foi Editar como ADM\n")

    arquivo = open("cadastroADM.txt", "r")
    listar = arquivo.readlines()
         
    cod_alterar = str(input("Digite o código do produto que deseja alterar: "))
    while cod_alterar not in codigo_produto:
        cod_alterar = str(input("[ERRO], por favor digite um código que exista: "))

    codigo_changer = codigo_produto.index(cod_alterar)
    print("\nA descrição atual do produto é %s" %(lista_produto[codigo_changer][1])) #amém, eu tive que criar 2 listas para que ess método funcionasse, uma com os código e uma com os pedidos

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
    print("teste\n")
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
    elif escolha == "3": #Se escolher sair...
        print("A opção desejada foi de sair")
        confirm = "n"
    else: #Se nenhuma das opções for correta:
        print("[ERRO] Dígito inválido \n")