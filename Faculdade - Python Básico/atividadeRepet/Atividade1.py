print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("1)Elaborar um algoritomo que leia um valor de tempratura em graus Celsius, calcule e exiba a temperatura equivalente em Kelvin, sabendo que: K = C = 273. Esse algoritmo deve repetir 5 vezes.\n")


for n in range (5):
    Cel = float(input("Por favor, digite uma temperatura em graus Celsius\n"))
    k = Cel + 273
    print("%0.2f°C é o equivalente a %0.2f°K\n" %(Cel, k))

    # *Exemplo feito em sala de Aula