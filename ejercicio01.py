def calculoMaxComDiv(a, b):
    while b:
        a, b = b, a % b
    return a

# prueba del caso
num1 = 1536
num2 = 2300
resultado = calculoMaxComDiv(num1, num2)
print(f"El Maximo Comun Divisor de {num1} y {num2} es {resultado}")