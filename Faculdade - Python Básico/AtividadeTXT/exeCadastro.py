print("Faça um cadastro de ADM e Operador:")

#variáveis

confirmar = "s"
caminho = "C:/Users/renat/OneDrive/Documentos/estudos/pyhton/Faculdade - Python Básico/AtividadeTXT/cadastroADM.txt"
confirm = "s"
codigo = 0 #"Boas práticas"
option = 0
optionAdm = 0
description = 0
price = 0
dados = []
temp = []
temp_cod = []

#funções

def menu(): #Menu, ele será a primeira coisa a ser chamada, retorna um input
    print("1) ADM")
    print("2) Operador")
    print("3) Sair \n")

    option = str(input("Digite qual opção deseja (escreva um número de 1 a 3): ")).strip()
    while option == "" and option != "1" and option != "2" and option != "3": #tirando erros
        option = str(input("Por favor, digite um número correto (de 1 a 3): "))

    return option

def menuADM():
    print("1) Cadastrar")
    print("2) Listar")
    print("3) Editar")
    print("4) Excluir")
    print("5) Sair \n")

    optionAdm = str(input("Digite qual opção deseja (escreva um número de 1 a 5): "))
    while optionAdm == "" and optionAdm != "1" and optionAdm != "2" and optionAdm != "3" and optionAdm != "4" and optionAdm != "5":
        optionAdm = str(input("Por favor, digite um número correto (de 1 a 5): "))

    return optionAdm

def CadastrarADM():
    codigo = 0
    arquivo = open(caminho, 'r', encoding='utf-8')
    dados = arquivo.readlines()
    if dados == []:
        codigo = 100
    else:
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')
            dados[i] = dados[i].split(';')
            temp.append(dados[i][0])
            arquivo.close()
 
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


    print("A opção escolhida foi cadastrar pedidos")
    print(f"Código do pedido: {codigo} \n")

    arquivo = open(caminho, "a")
    description = str(input("Descreva o arquivo a ser computado: "))
    price = str(input("Digite qual será o preço do produto: "))
    arquivo.write(f"{codigo} ; {description} ; {price} \n")
    arquivo.close()
    print("Arquivo gerado com sucesso!")

def ListarADM():
    print("teste \n")

def EditarADM():
    print("teste\n")

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
                print("A opção desejada foi de cadastrar no modo ADM\n")
                CadastrarADM()
            elif escolhaAdm == "2":
                print("A opção desejada foi de Listar como ADM\n")
                ListarADM()
            elif escolhaAdm == "3":
                print("A opção desejada foi Editar como ADM\n")
                EditarADM()
            elif escolhaAdm == "4":
                print("A opção desejada foi de Excluir com ADM\n")
                ExcluirADM()
            elif escolhaAdm == "5":
                print("A opção desejada foi de sair do modo ADM\n")
                break
            else:
                print("[ERRO] digite um número válido (1 a 5): ")

    elif escolha == "2": #Se escolher operador... #se for 2, modo Operador
        print("A opção desejada foi de entrar como ADM \n")
    elif escolha == "3": #Se escolher sair...
        print("A opção desejada foi de sair")
        confirm = "n"
    else: #Se nenhuma das opções for correta:
        print("[ERRO] Dígito inválido \n")