def contar_palabras(cadena):
    # Convertir la cadena a minúsculas para hacer la contabilidad insensible a mayúsculas/minúsculas
    cadena = cadena.lower()
    
    # Remover los signos de puntuación (opcional, para contar solo palabras)
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

# Ejemplo de uso
cadena = "Hola, hola! ¿Como estas? Yo estoy bien, bien, bien."
frecuencia = contar_palabras(cadena)
print(frecuencia)