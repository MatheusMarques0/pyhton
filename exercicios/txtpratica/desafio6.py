confirmar = "1"

def decrescente():
    x = 100

    arquivo = open ("numeros.txt", "a+")
    for n in range(100):
        arquivo.write(str(f"{x}" + "\n"))
        x = x - 1

#Main

while confirmar == "1":
    decrescente()

    conf = str(input("Você quer que a repetição pare? (0 - sim / qualquer outro número - não): "))
    while conf == "":
        conf = str(input("[ERRO] Não deixe a resposta vazia: "))
    
    if conf == "0":
        print("A opção desejada foi de encerrar a repetição!")
        confirmar = "2"
    else:
        print("A opção desejada foi de continuar registrando!")