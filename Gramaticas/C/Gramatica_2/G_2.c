/*
Objetivo:
    Revisar si la cadena pertenece a L(g2) = {a^n b^(n+1) | n >= 0}.
*/

#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("G_2.txt", "r");
    char cadena[100];
    
    while (fgets(cadena, 100, archivo)) {
        cadena[strcspn(cadena, "\n")] = 0;
        int n = strlen(cadena);
        
        int i = 0;
        while (i<n && cadena[i]=='a') i++;
        int n_a = i;
        
        int n_b = n - n_a;
        int solo_b = 1;
        for (int j=i; j<n; j++) {
            if (cadena[j] != 'b') solo_b = 0;
        }
        
        if (solo_b && n_b == n_a + 1) {
            printf("%s acepta\n", cadena);
        } else {
            printf("%s NO acepta\n", cadena);
        }
    }
    fclose(archivo);
    return 0;
}
