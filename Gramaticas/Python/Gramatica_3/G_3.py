"""
Objetivo:
    Revisar si la cadena pertenece a L(g3) = {a^n b^(n+1) | n > 0}.

Entrada:
    Archivo "G_3.txt".

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
"""

archivo = open("G_3.txt")

for linea in archivo:
    cadena = linea.strip()
    
    # contar 'a'
    n_a = 0
    for c in cadena:
        if c == 'a':
            n_a += 1
        else:
            break
    
    resto = cadena[n_a:]
    n_b = len(resto)
    solo_b = all(c == 'b' for c in resto)
    
    if n_a > 0 and solo_b and n_b == n_a + 1:
        print(cadena, "acepta")
    else:
        print(cadena, "NO acepta")

archivo.close()
