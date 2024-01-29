#include <stdio.h>

int main() {
    // Generate values for n
    int n_values[] = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    int num_values = sizeof(n_values) / sizeof(n_values[0]);

    // Calculate corresponding x(n) values
    int x_values[num_values];
    for (int i = 0; i < num_values; i++) {
        x_values[i] = (n_values[i] * n_values[i] * n_values[i] + 2 * n_values[i] * n_values[i] +
                       5 * n_values[i] + 80) * (n_values[i] >= 0);
    }

    // Create and open a file for writing
    FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    // Write values to the file
    for (int i = 0; i < num_values; i++) {
        fprintf(file, "%d %d\n", n_values[i], x_values[i]);
    }

    // Close the file
    fclose(file);

    return 0;
}
