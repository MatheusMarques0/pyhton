print('Atividade 2')

numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é maior que zero
if numero <= 0:
    print("Por favor, insira um número positivo.")
else:
    # Verificação se o número é primo
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo and numero > 1:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo. Seus divisores são:")
        # Exibe os divisores do número
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i)