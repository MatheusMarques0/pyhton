#4. Crie um programa que recebe nomes inteiros e os coloca em linhas separadas chamado nomes.txt, pegue essa lista e tire todos os espaços, crie um segundo txt com sem os espaços nos nomes.

#var
nomes = []
nomes_strip = []
listas = []

#fun

def Cadastrar():
    nomes.clear()
    num = int(input("Quantos nomes você quer? "))
    while num <= 0:
        num = int(input("[ERRO] Número inválido, digite um número maior que 0: "))
    
    for n in range(num):
        name = str(input("Digite um nome: "))
        nomes.append(name)

    with open ("nomes.txt", "a") as arquivo:
        for n in range(num):
            arquivo.write(str(nomes[n] + "\n"))

    print("Arquivo gerado com sucesso")

def Editar():
    nomes.clear()
    num = int(input("Quantos nomes você quer? "))
    while num <= 0:
        num = int(input("[ERRO] Número inválido, digite um número maior que 0: "))
    
    for n in range(num):
        name = str(input("Digite um nome: "))
        nome = name.strip()
        nomes_strip.append(nome)

    with open ("nomes_strip.txt", "a") as arquivo:
        for n in range(num):
            arquivo.write(str(nome+ "\n"))

    print("Arquivo gerado com sucesso")

print("Desafio 4")
opt = str(input("Cadastrar nomes ou escrever sem espaços? (1 - Cadastar / 2- sem espaços): "))
while opt != "1" and opt != "2":
    opt = str(input("[ERRO] Por favor, digite um número válido (1 / 2): "))

if opt == "1":
    print("Você escolheu cadastar")
    Cadastrar()
else:
    print("Você escolheu Editar \n")
    Editar()