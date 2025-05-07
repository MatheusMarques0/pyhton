print("Exercícios - Repetição com while (Pyhton) \n")

print("1)Elaborar um programa que solicita várias temperaturas em graus Celsius. Para cada temperatura inserida, o programa deve converter para graus Fahrenheint e Kelvin e mostrar na tela. O programa termina quando a temperatura inserida for menor que -5. \n")

cel = float(input("Digite uma temperatura em Celsius: \n"))

while (cel > -5 ):
    F = ( cel * 1.8 ) + 32
    K = cel + 273
    print(f"A temperatura {cel} em Fahrenheint é {F} e em Kelvin é {K}.")
    cel = float(input("Digite outra: \n"))

print("Fim.")