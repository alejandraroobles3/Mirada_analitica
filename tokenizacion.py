import re
import string

def eliminar_emojis(texto):
    # Eliminar emojis utilizando una expresión regular
    patron_emojis = re.compile("["
                              u"\U0001F600-\U0001F64F"  # emoticones
                              u"\U0001F300-\U0001F5FF"  # símbolos e iconos
                              u"\U0001F680-\U0001F6FF"  # transporte y mapas
                              u"\U0001F700-\U0001F77F"  # alquimia
                              u"\U0001F780-\U0001F7FF"  # alquimia (extensión A)
                              u"\U0001F800-\U0001F8FF"  # puntos de código de compatibilidad suplementaria
                              u"\U0001F900-\U0001F9FF"  # emoji complementarios y pictogramas
                              u"\U0001FA00-\U0001FA6F"  # emoji de personas
                              u"\U0001FA70-\U0001FAFF"  # alquimia (extensión B)
                              u"\U00002702-\U000027B0"  # adiciones de emoji
                              u"\U000024C2-\U0001F251" 
                              "]+", flags=re.UNICODE)
    
    # Reemplazar emojis con espacios en blanco
    texto_sin_emojis = re.sub(patron_emojis, '', texto)
    
    return texto_sin_emojis

def remove_punctuation(text):
    """Función para eliminar la puntuación"""
    return text.translate(str.maketrans('', '', string.punctuation))

def procesar_archivo_entrada(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    lineas_procesadas = [remove_punctuation(eliminar_emojis(linea)) for linea in lineas if linea.strip()]  # Eliminar renglones en blanco
    
    return lineas_procesadas

def guardar_archivo_salida(nombre_archivo, lineas_procesadas):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.writelines(lineas_procesadas)

# Ejemplo de uso
nombre_archivo_entrada = 'txt/claudia.txt'
nombre_archivo_salida = 'txt/udg.txt'

lineas_procesadas = procesar_archivo_entrada(nombre_archivo_entrada)
guardar_archivo_salida(nombre_archivo_salida, lineas_procesadas)

print(f"Proceso completado. Texto procesado guardado en {nombre_archivo_salida}")
