print("Exercícios - String")

print("Elaborar um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita (Exemplo: ovo, ana). \n")

palavra = str(input("Digite um nome: \n"))

if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é um palíndromo.")
else:
    print(f"A palavra {palavra} não é um palindromo.")