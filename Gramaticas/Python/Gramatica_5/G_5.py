"""
Objetivo:
    Revisar si la cadena pertenece a L(g5) = {a (ab)^n b | n >= 0}.

Entrada:
    Archivo "g5.txt".

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
"""

archivo = open("g5.txt")

for linea in archivo:
    cadena = linea.strip()
    
    if not (cadena.startswith("a") and cadena.endswith("b")):
        print(cadena, "NO acepta")
        continue
    
    # quitamos la primera 'a' y la última 'b'
    centro = cadena[1:-1]
    
    es_valida = True
    while centro != "":
        if centro.startswith("ab"):
            centro = centro[2:]
        else:
            es_valida = False
            break
    
    if es_valida:
        print(cadena, "acepta")
    else:
        print(cadena, "NO acepta")

archivo.close()
