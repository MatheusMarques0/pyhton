print("Exercícios - Repetição com while (Pyhton) \n")

print("2) elaborar um algoritmo que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. O programa deve repetir até que o usuário digite um número fora desse intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando 'Número inválido'. \n")

num = int(input("Digite um número entre 1 e 7: \n"))

while (num >= 1 and num <= 7):
    
    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Segunda-Feira")
    elif num == 3:
        print("Terça-Feira")
    elif num == 4:
        print("Quarta-Feira")
    elif num == 5:
        print("Quinta-Feira")
    elif num == 6:
        print("Sexta-Feira")
    else:
        print("Sábado")
    
    num = int(input("Digite outro número: "))

else:
    print("número inválido")