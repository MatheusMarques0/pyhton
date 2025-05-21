print("3)Desenvolva um programa que cadastra alunos.")

#Variáveis

confirm = "s"

aluno = []

#Funções

def menu():
    print("1) Cadastrar novo aluno")
    print("2) Listar alunos cadastrados")
    print("3) Buscar aluno")
    print("4) Remover aluno")
    print("5) Sair")
    option = str(input("Digite qual opção deseja (escreva um número de 1 a 5)."))
    while option == "" and option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
        option = str(input("Por favor, digite um número correto (de 1 a 5): "))

    return option

def cadastro():
    arquivo = open("C:/Users/renat/OneDrive/Documentos/estudos/pyhton/Faculdade - Python Básico/AtividadeTXT/cadastro.txt", "a")
    nome = str(input("Digite o nome do aluno a ser cadastrado: "))
    arquivo.write(str("nome:" + nome + " "))
    email = str(input("Digite o e-mail do aluno a ser cadastrado: "))
    arquivo.write(str("e-mail:" + email + " "))
    curso = str(input("Digite o curso do aluno"))
    arquivo.write(str("curso:" + curso + " ") + "\n")
    arquivo.close()
    print("\nArquivo gerado com sucesso!")

def listar():
    s

def buscar():
    w

def remove():
    s

#Main

while confirm == "s":

    escolha = menu()

    if escolha == "1":
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

