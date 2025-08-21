/*
Objetivo:
    Revisar si la cadena pertenece a L(g4) = {abb, ab}.
*/

#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("G_4.txt", "r");
    char cadena[100];
    
    while (fgets(cadena, 100, archivo)) {
        cadena[strcspn(cadena, "\n")] = 0;
        
        if (strcmp(cadena, "abb") == 0 || strcmp(cadena, "ab") == 0) {
            printf("%s acepta\n", cadena);
        } else {
            printf("%s NO acepta\n", cadena);
        }
    }
    fclose(archivo);
    return 0;
}
