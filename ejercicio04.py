def contar_palabras(cadena):
    # Convertir la cadena a minúsculas para hacer la contabilidad insensible a mayúsculas/minúsculas
    cadena = cadena.lower()
    
    # Remover los signos de puntuación
    import string
    cadena = cadena.translate(str.maketrans("", "", string.punctuation))
    
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Crear un diccionario para contar la frecuencia de cada palabra
    frecuencia_palabras = {}
    
    # Contar las palabras
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    return frecuencia_palabras

def palabra_mas_repetida(diccionario_frecuencia):
    # Inicializar variables para almacenar la palabra más repetida y su frecuencia
    palabra_max = None
    frecuencia_max = 0
    
    # Iterar sobre el diccionario para encontrar la palabra con la frecuencia más alta
    for palabra, frecuencia in diccionario_frecuencia.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    return (palabra_max, frecuencia_max)


# Cadena de ejemplo
cadena = "Messi campeon del mundo MEssi campeon Argentina Boca paraguay ArGentiNa Japon. Liguilla clausura python anywhere messi"

# Llamar a la función para contar las palabras
frecuencia = contar_palabras(cadena)
print("Frecuencia de palabras:", frecuencia)

# Llamar a la función para encontrar la palabra más repetida
palabra_frecuente = palabra_mas_repetida(frecuencia)
print("Palabra mas repetida y su frecuencia:", palabra_frecuente)