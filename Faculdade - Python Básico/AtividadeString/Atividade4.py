print("Exercícios - String")

print("4) Elaborar um programa que receba o usuário uma string. O programa deve imprimir a string sem suas vogais")

conso = []
vol = []

pal = str(input("Digite uma palavra: \n")) #input

tamanhoPAL = len(pal) #tamanho da palvra

y = 0 #ponteiro

for n in range(tamanhoPAL): #uma repetição para cada letra
    letra = pal[y] #definindo as letras em palavra

    if letra != "a" and letra != "A" and letra != "E" and letra != "e" and letra != "I" and letra != "i" and letra != "O" and letra != "o" and letra != "U" and letra != "u": #conferindo se a letra é uma consoante

        conso.append(letra) #se for consoante, adicione em consol
    else:
        vol.append(letra) #se for vogal, aiciona em vogal

    y = y + 1
        
print(f"{conso}")