def get_init_recursivo():
    try:
        valor = int(input("Por favor, introduce un numero entero: "))
        return valor
    except ValueError:
        print("Valor no valido. Intentalo de nuevo.")
        return get_init_recursivo()


# Ejemplo de uso
numero = get_init_recursivo()
print("Número introducido:", numero)
