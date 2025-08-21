"""
Objetivo:
    Revisar si la cadena es capicúa (palíndromo) formada solo por 0 y 1.

Entrada:
    Archivo "G_1.txt", una cadena por línea.

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
"""

# Abrimos el archivo
archivo = open("G_1.txt", "r")

for linea in archivo:
    cadena = linea.strip()  # quitamos salto de línea
    
    # bandera binario
    binario = True
    
    for c in cadena:
        if c != '0' and c != '1':
            binario = False
            break
    
    # verificamos que sea palíndromo
    palindromo = (cadena == cadena[::-1])
    
    if binario and palindromo:
        print(cadena, "acepta")
    else:
        print(cadena, "NO acepta")

archivo.close()
