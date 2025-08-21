"""
Objetivo:
    Revisar si la cadena pertenece a L(g2) = {a^n b^(n+1) | n >= 0}.

Entrada:
    Archivo "g2.txt".

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
"""

archivo = open("g2.txt")

for linea in archivo:
    cadena = linea.strip()
    
    # contamos cuántas 'a' seguidas hay al inicio
    n_a = 0
    for c in cadena:
        if c == 'a':
            n_a += 1
        else:
            break
    
    # el resto deben ser solo 'b'
    resto = cadena[n_a:]
    n_b = len(resto)
    solo_b = all(c == 'b' for c in resto)
    
    if solo_b and n_b == n_a + 1:
        print(cadena, "acepta")
    else:
        print(cadena, "NO acepta")

archivo.close()
