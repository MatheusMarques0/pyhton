print("Exercícios - Repetição com while (Pyhton) \n")

print("5)Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2 deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até N. \n")

N = int(input("Digite um número maior que 2: \n"))

x = 0
start = 1

while (N <= 2):
    N = int(input("Digite outro número maior que 2, por favor: \n"))
    
while (x < N):
    new = x + 1
    quadrado = new * new
    cubo = new * new * new
    print(f"O quadrado de {new} é {quadrado}, o seu cubo é {cubo}")
    x = x + 1

else:
    print("\nFim.")