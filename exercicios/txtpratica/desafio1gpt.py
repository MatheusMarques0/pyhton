def carros():

    carro1 = str(input("Digite um modelo de carro: "))
    carro2= str(input("Digite outro de carro: "))
    carro3 = str(input("Digite outro de carro: "))
    car = str(input("Quantos carros você tem? \n"))

    with open('texto1.txt', 'a') as arquivo:
        arquivo.write(str(carro1 + ";" + carro2 + ";" + carro3 + ";" + f"{car}" + "\n"))

    print("Arquivo gerado com sucesso!")

def prints():

    with open('texto1.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for n in range(len(linhas)):
            print(f"{linhas[n]}")

def lists():

    with open('texto1.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        print(len(linhas))

opt = str(input("Qual escolha deseja fazer agora? 1/2/3: "))

if opt == "1":
    carros()
elif opt == "2":
    prints()
else:
    lists()