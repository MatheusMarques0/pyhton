print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("3) Elaborar um algoritimo que recebe 3 valores (A, B e C) e exibe qual é o maior entre eles. Esse programa deve-se repetir 20 vezes.\n")

for n in range (20):
    A = float(input("Digite o valor A\n"))
    B = float(input("Digite o valor B\n"))
    C = float(input("Digite o valor C\n"))


    if A == B or A == C or B == C:
            print("Há números repetidos! Por favor, Digite 3 números distintos")
    else:
        if A > B and A > C:
            print(f"{A} é o maior número")
        elif B > A and B > C:
            print(f"{B} é o maior número")
        else:
            print(f"{C} é o maior número")