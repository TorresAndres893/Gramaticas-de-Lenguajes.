/*
Objetivo:
    Revisar si la cadena pertenece a L(g5) = {a (ab)^n b | n >= 0}.

Entrada:
    Archivo "G_5.txt".

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
*/

#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("G_5.txt", "r");
    if (!archivo) {
        printf("No se pudo abrir el archivo.\n");
        return 1;
    }

    char cadena[100];
    while (fgets(cadena, sizeof(cadena), archivo)) {
        cadena[strcspn(cadena, "\n")] = 0; // quitar salto de línea
        int n = strlen(cadena);

        // condición básica
        if (n < 2 || cadena[0] != 'a' || cadena[n-1] != 'b') {
            printf("%s NO acepta\n", cadena);
            continue;
        }

        int valido = 1;
        int i = 1;  // empezamos después de la 'a' inicial
        while (i < n-1) {  // hasta antes de la 'b' final
            // si quedan menos de 2 caracteres en el centro → no es válido
            if (i + 1 >= n-1) {
                valido = 0;
                break;
            }

            if (cadena[i] == 'a' && cadena[i+1] == 'b') {
                i += 2; // consumimos un "ab"
            } else {
                valido = 0;
                break;
            }
        }

        if (valido)
            printf("%s acepta\n", cadena);
        else
            printf("%s NO acepta\n", cadena);
    }

    fclose(archivo);
    return 0;
}
