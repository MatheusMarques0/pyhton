print("3)Desenvolva um programa que cadastra alunos.")

#Variáveis

confirm = "s"

aluno = []
student = []

#Funções

def menu(): #Menu, ele será a primeira coisa a ser chamada, retorna um input
    print("1) Cadastrar novo aluno")
    print("2) Listar alunos cadastrados")
    print("3) Buscar aluno")
    print("4) Remover aluno")
    print("5) Sair")
    option = str(input("Digite qual opção deseja (escreva um número de 1 a 5)."))
    while option == "" and option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
        option = str(input("Por favor, digite um número correto (de 1 a 5): "))

    return option

def cadastro(): #Abre arquivo, pega nome, coloca no arquivo, repita.
    arquivo = open("C:/Users/renat/OneDrive/Documentos/estudos/pyhton/Faculdade - Python Básico/AtividadeTXT/cadastro.txt", "w")
    nome = str(input("Digite o nome do aluno a ser cadastrado: "))
    arquivo.write(str("nome:" + nome + " "))
    email = str(input("Digite o e-mail do aluno a ser cadastrado: "))
    arquivo.write(str("e-mail:" + email + " "))
    curso = str(input("Digite o curso do aluno"))
    arquivo.write(str("curso:" + curso + " ") + "\n")
    arquivo.close()
    print("\nArquivo gerado com sucesso!")

def listar(): 
    arquivo = open("C:/Users/renat/OneDrive/Documentos/estudos/pyhton/Faculdade - Python Básico/AtividadeTXT/cadastro.txt", "r")
    listar = arquivo.readlines() #Irá ler linha por linha
    tamanholistar = len(listar) #Tamanho do arquivo
    for n in range(tamanholistar): #Ponteiro para a repetição
        linha = listar[0] #Pega o primeiro termo da lista (o primeiro cadastro, no caso), inicialmente eu estava com problemas por colocar [listar[0]] com duas chaves [], mas pelo visto isso torna linha uma lista, e listas não podem usar .find(), algo para se anotar.
        start_fulano = linha.find("nome:") + len("nome:") #Acha a palavra nome, tem indice 0, por isso coloquei + len("nome"), quero saber o nome do aluno, não "nome:fulano". Poderia ter colocado só 5 também, mas ficaria menos escalavel.
        end_fulano = linha.find("e-mail:") #Vai achar o índice do email, ou seja, quando ele começa
        name = linha[start_fulano:end_fulano].strip() #O professor ensinou esse método em sala da aula, ele vai do ponto A até o B da lista, no caso, onde começa o nome e onde começa o email. Eu não sei se o professor ensinou o strip em sala de aula, mas eu vi isso naquele desafio da Erika junto com o Luigi :D
        print(name) #Vai retornar o nome do aluno
    arquivo.close()

def buscar():
    w

def remove():
    s

#Main

while confirm == "s":

    escolha = menu() # mostrará o menu, e o resultado virará uma variável

    if escolha == "1": #dependendo da escolha o comando irá fazer algo
        print("A opção desejada foi fazer o cadastro de um novo aluno \n")
        cadastro()
    elif escolha == "2":
        print("A opção desejada foi de listar os alunos cadastrados \n")
        listar()
    elif escolha == "3":
        print("A opção desejada foi de listar os alunos cadastrados \n")
        buscar()
    elif escolha == "4":
        print("A opção desejada foi de listar os alunos cadastrados \n")
        remove()
    else:
        print("Aplicação terminada")
        confirm = "n"

