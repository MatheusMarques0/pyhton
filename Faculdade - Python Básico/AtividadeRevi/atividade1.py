print('Atividade 2')

lado1=float(input("Escreva o lado 1 do triangulo: "))
lado2=float(input("Escreva o aldo 2 do trianuglo: "))
lado3=float(input("Escreva o lado 3 do trinagulo: "))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print("Triângulo inválido, lmao")
elif lado1 == lado2 and lado1 == lado3:
    print("Trinângulo Equilatero")
elif lado1 == lado2 or lado1 == lado3:
    print("Triânguolo Isósceles")
else:
    print("Triângulo Escaleno")