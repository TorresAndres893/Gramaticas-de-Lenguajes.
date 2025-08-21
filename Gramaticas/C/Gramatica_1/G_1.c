/*
Objetivo:
    Revisar si la cadena es capicúa (palíndromo) y solo usa 0 y 1.

Entrada:
    Archivo "g1.txt".

Salida:
    "<cadena> acepta" o "<cadena> NO acepta".
*/

#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("G_1.txt", "r");
    char cadena[100];
    
    while (fgets(cadena, 100, archivo)) {
        cadena[strcspn(cadena, "\n")] = 0; // quitar salto
        
        int n = strlen(cadena);
        int es_binaria = 1;
        int es_palindromo = 1;
        
        for (int i=0; i<n; i++) {
            if (cadena[i] != '0' && cadena[i] != '1') {
                es_binaria = 0;
            }
        }
        for (int i=0; i<n/2; i++) {
            if (cadena[i] != cadena[n-1-i]) {
                es_palindromo = 0;
            }
        }
        
        if (es_binaria && es_palindromo) {
            printf("%s acepta\n", cadena);
        } else {
            printf("%s NO acepta\n", cadena);
        }
    }
    fclose(archivo);
    return 0;
}
