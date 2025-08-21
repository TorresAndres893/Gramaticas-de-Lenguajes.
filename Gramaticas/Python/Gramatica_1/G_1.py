"""
Objetivo:
    Revisar si la cadena es capicúa (palíndromo) formada solo por 0 y 1.

Entrada:
    Archivo "G_1.txt", una cadena por línea.

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
"""

# Abrimos el archivo
archivo = open("G_1.txt")

for linea in archivo:
    cadena = linea.strip()  # quitamos salto de línea
    
    # verificamos que solo contenga 0 y 1
    es_binaria = all(c in "01" for c in cadena)
    
    # verificamos que sea palíndromo
    es_palindromo = (cadena == cadena[::-1])
    
    if es_binaria and es_palindromo:
        print(cadena, "acepta")
    else:
        print(cadena, "NO acepta")

archivo.close()
