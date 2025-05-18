print("Fazendo uma calculadora")

operador = ["somado", "subtraído", "multiplicado", "dividido", "elevado"]

def adicao(num1, num2):
    print(f"O número {num1} {operador[x]} por {num2} é igual a:", num1 + num2)

def sub(num1, num2):
    print(f"O número {num1} {operador[x]} por {num2} é igual a:", num1 - num2)

def multi(num1, num2):
    print(f"O número {num1} {operador[x]} por {num2} é igual a:", num1 * num2)

def div(num1, num2):
    print(f"O número {num1} {operador[x]} por {num2} é igual a:", num1 / num2)

def expo(num1, num2):
    print(f"O número {num1} {operador[x]} por {num2} é igual a:", num1 ** num2)

num1 = float(input("Digite um número: "))

print("Qual das funções você deseja usar? \n")

print("1) ", operador[0])
print("2) ", operador[1])
print("3) ", operador[2])
print("4) ", operador[3])
print("5) ", operador[4])

escolha = int(input("(digite de 1 - 5): "))

while escolha < 1 or escolha > 5:
    escolha = float(input("[ERRO] Número inválido, Digite um número entre 1 e 5"))

if escolha == 1:
    x = 0
elif escolha == 2:
    x = 1
elif escolha == 3:
    x = 2
elif escolha == 4:
    x = 3
else:
    x = 4

num2 = float(input(f"Digite um número: para ser {operador[x]}: "))

if escolha == 1:
    adicao(num1, num2)
elif escolha == 2:
    sub(num1, num2)
elif escolha == 3:
    multi(num1, num2)
elif escolha == 4:
    div(num1, num2)
else:
    expo(num1, num2)