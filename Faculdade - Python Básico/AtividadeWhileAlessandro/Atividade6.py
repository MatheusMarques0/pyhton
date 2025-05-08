print("Exercícios - Repetição com while (Pyhton)\n")

print("6) Elaborar um programa que solicita um número (entre 10 a 15). Se o usuário digitar um número diferente, o programa deve mostrar a mensagem 'Entrada inválida' e solicitar um número novamente. Se digitar correto o programa deve mostrar a raiz quadrada desse número e termina.\n")

num = float(input("Digite um número entre 10 e 15, por favor:\n"))

while (num < 10 or num > 15):
    num = float(input("Entrada inválida, por favor digite outro número:\n"))

else:
    raiz = num ** 0.5
    print("a raíz quadrada do número é %0.2f" %(raiz))