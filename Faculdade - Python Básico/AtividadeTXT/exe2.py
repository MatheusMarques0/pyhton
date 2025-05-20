print("2)Desenvolva um algoritmo que escreve em disco um arquivo com números ordenados decrescentemente de 100 a 1. Cada número deve estar em uma linha. O arquivo deve se chamar 'decrescente.txt'. \n")

lista = []

arquivo = open("C:/Users/renat/OneDrive/Documentos/estudos/pyhton/Faculdade - Python Básico/AtividadeTXT/decrescente.txt", "w")

n = 101

while n > 0:
    if n > 1:
        arquivo.writelines(str(n - 1) + "; \n")
    else:
        arquivo.writelines(str(n - 1) + ". \n")

    n = n - 1

arquivo.close()

print("Arquivo gerado.")