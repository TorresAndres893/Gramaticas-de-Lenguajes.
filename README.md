# Gramaticas-de-Lenguajes.
## Objetivo

Implementar programas en **C** y en **Python** que revisen si cadenas de texto cumplen con las gramáticas definidas en la presentación 1.
Cada programa lee un archivo de entrada (`.txt`) y muestra por pantalla si la cadena **"acepta"** o **"NO acepta"**.

---

## Gramáticas trabajadas

1. **g1**

   ```
   S → 0 S 0 | 1 S 1 | 0 | 1
   ```

   Lenguaje: números capicúas (palíndromos) de 0 y 1.

2. **g2**

   ```
   S → a S b | b
   ```

   Lenguaje: a^n b^(n+1), con n ≥ 0.

3. **g3**

   ```
   S → a S b | abb
   ```

   Lenguaje: a^n b^(n+1), con n > 0.

4. **g4**

   ```
   S → ab | abb
   ```

   Lenguaje: cadenas fijas {ab, abb}.

5. **g5**

   ```
   S → a T b
   T → ab T | ε
   ```

   Lenguaje: a (ab)^n b, con n ≥ 0.

---

## Ejecución

### En C

1. Compilar el programa correspondiente, por ejemplo:

   ```
   gcc (nombre_archivo).c -o (nombre_archivo)
   ```
2. Ejecutar el binario:

   ```
   ./(nombre_archivo)
   ```

### En Python

1. Ejecutar el programa directamente:

   ```
   python3 (nombre_archivo).py
   ```

## Notas
