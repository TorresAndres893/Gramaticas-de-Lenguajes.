"""
Objetivo:
    Revisar si la cadena pertenece a L(g4) = {abb, ab}.

Entrada:
    Archivo "g4.txt".

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
"""

archivo = open("g4.txt")

for linea in archivo:
    cadena = linea.strip()
    
    if cadena == "abb" or cadena == "ab":
        print(cadena, "acepta")
    else:
        print(cadena, "NO acepta")

archivo.close()
