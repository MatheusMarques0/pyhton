print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("2)Elaborar um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é múltiplo de 3 e se é positivo ou negativo. Esse programa deve-se repetir 6 vezes\n")

for n in range (6):
    i = int(input("Escreva um número inteiro... e adivinharei se ele é múltiplo de 3, positivo ou negativo!"))
    if i == 0:
        print("Ora, você está tentando me fazer uma pegadinha? Zero não conta!")
    else:
        if i % 3 == 0:
            print("Este número é múltiplo de 3!")
        else:
            print("Este número não é múltiplo de 3!")

        if i < 0:
            print("Este número é negativo!")
        else:
            print("Este númeto é postivo!")