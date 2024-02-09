#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("data4.dat", "w");  // Open file for writing
    
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    // Generate data and write to file
    for (int n = -3; n <= 11; n++) {
        double yn;
        if (n >= 0) {
            yn = 1.5 * (n * n + 3 * n + 2);
        } else {
            yn = 0.0;
        }
        fprintf(fp, "%5d %10.2lf\n", n, yn);
    }
    
    fclose(fp);  // Close file
    return 0;
}
