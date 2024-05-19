def get_init_iterativo():
    while True:
        try:
            valor = int(input("Por favor, introduce un numero entero: "))
            return valor
        except ValueError:
            print("Valor no valido. Intentalo de nuevo.")


# Ejemplo de uso
numero = get_init_iterativo()
print("Número introducido:", numero)
