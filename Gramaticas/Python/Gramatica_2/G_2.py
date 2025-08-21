# Objetivo:
# Checar si la cadena está en el lenguaje:
# L(g2) = { a^n b^(n+1) | n >= 0 }
#
# Gramática:
# S → a S b | b

archivo = open("G_2.txt")

for linea in archivo:
    texto = linea.strip()
    
    # Contar las 'a' al principio
    numero_a = 0
    for letra in texto:
        if letra == 'a':
            numero_a += 1
        else:
            break

    restante = texto[numero_a:]
    
    # Contar las 'b'
    numero_b = len(restante)
    
    # Fijarse si todo lo que sobra es 'b'
    b = True
    for letra in restante:
        if letra != 'b':
            b = False
            break

    # Checar las reglas:
    # 1. Todo lo que sobra tiene que ser 'b'
    # 2. Tiene que haber una 'b' más que 'a'
    if b and numero_b == numero_a + 1:
        print(texto, "→ SÍ")
    else:
        print(texto, "→ NO")

# Cerrar el archivo
archivo.close()
