print("Atividade 1: Exercícios - Estrutura de Repetição - PARA (atividade do dia 24/04)\n")

print("5)Elaborar um algoritmo que soicite ao usuário para digitar 15 valores e deve exibir a soma e média\n")

valores = []

for n in range (15):
    val = float(input("Digite um valor para ser usado\n"))
    valores.append(val)

soma = sum(valores)

media  = soma / 15

print(f"a soma dos números é {soma}, e a média é {media}")