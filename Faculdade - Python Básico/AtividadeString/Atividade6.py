print("Exercícios - String")

print("Elaborar um programa que o usuário deve preencher uma lista com os modelos de cinco carros. O usuário também deve preencher outra lista com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível. Calcule e mostre: \n")

print("(a) O modelo de carro mais econômico: \n")

print("(b) Quantos litros de combutível cada um dos carros cadastrados consome para percorrer uma distância de 1.000 quilômetros.\n")

carros = []

consumo = []

distancia = []

for n in range(5):
    car = str(input('Digite um modelo de carro: \n'))
    carros.append(car)

    cons = float(input("Digite o consumo de desse carro por kilômetros por litro: \n"))
    consumo.append(cons)
    distan = 1000 / cons
    distancia.append(distan)

menor = min(consumo)
posi = consumo.index(menor)
modelo = carros[posi]

print(f"o carro mais ecônomico é o {modelo}, com {menor} litros consumido por km \n")

x = 0

for n in range(5):
    print("o %s consome %0.2f litros de gasolina para 1.000 kilômetros \n" % (carros[x], distancia[x]))
    x = x + 1