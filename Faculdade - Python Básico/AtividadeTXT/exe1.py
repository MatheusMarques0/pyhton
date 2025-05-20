print("1) Desenvolva um algoritmo que escreve em disco um arquivo com números ordenados crescentemente de 1 a 100. Cada número deve ser separado por ','. O arquivo deve se chamar 'crescente.txt'. \n")

lista = []

arquivo = open("C:/Users/renat/OneDrive/Documentos/estudos/pyhton/Faculdade - Python Básico/AtividadeTXT/crescente.txt", "w")

for n in range(100):
    if n < 99:
        arquivo.write(str(n + 1) + ";")
    else:
        arquivo.write(str(n + 1) + ".")

arquivo.close()

print("Arquivo gerado.")