def calculoMinComMul(a, b):
    return abs(a * b) // calculoMaxComDiv(a, b)


def calculoMaxComDiv(a, b):
    while b:
        a, b = b, a % b
    return a


# prueba del caso
num1 = 10
num2 = 20
resultado = calculoMinComMul(num1, num2)
print(f"El Minimo Comun Multiplo entre {num1} y {num2} es {resultado}")
