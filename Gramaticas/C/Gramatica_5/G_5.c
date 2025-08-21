/*
Objetivo:
    Revisar si la cadena pertenece a L(g5) = {a (ab)^n b | n >= 0}.
*/

#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("G_5.txt", "r");
    char cadena[100];
    
    while (fgets(cadena, 100, archivo)) {
        cadena[strcspn(cadena, "\n")] = 0;
        int n = strlen(cadena);
        
        if (n < 2 || cadena[0] != 'a' || cadena[n-1] != 'b') {
            printf("%s NO acepta\n", cadena);
            continue;
        }
        
        int es_valida = 1;
        for (int i=1; i<n-1; ) {
            if (cadena[i]=='a' && cadena[i+1]=='b') {
                i += 2;
            } else {
                es_valida = 0;
                break;
            }
        }
        
        if (es_valida) {
            printf("%s acepta\n", cadena);
        } else {
            printf("%s NO acepta\n", cadena);
        }
    }
    fclose(archivo);
    return 0;
}
