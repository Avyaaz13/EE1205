#include <stdio.h>
#include <math.h>

// Function to calculate steady-state error for original PID gains
double steady_state_error_original(double Ki) {
    return 2.0 / Ki;
}

// Function to calculate steady-state error for adjusted PID gains
double steady_state_error_adjusted(double Ki) {
    return 2.0 / (3 * Ki);
}

int main() {
    FILE *fp;
    double Ki_values[100];
    double original_errors[100];
    double adjusted_errors[100];
    int i;

    // Generate a range of Ki values
    for (i = 0; i < 100; i++) {
        Ki_values[i] = 0.1 + 10.0 * i / 99.0;
    }

    // Calculate steady-state errors for original PID gains
    for (i = 0; i < 100; i++) {
        original_errors[i] = steady_state_error_original(Ki_values[i]);
    }

    // Calculate steady-state errors for adjusted PID gains
    for (i = 0; i < 100; i++) {
        adjusted_errors[i] = steady_state_error_adjusted(Ki_values[i]);
    }

    // Write the coordinates to a data file
    fp = fopen("steady_state_errors.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (i = 0; i < 100; i++) {
        fprintf(fp, "%lf %lf %lf\n", Ki_values[i], original_errors[i], adjusted_errors[i]);
    }

    fclose(fp);

    printf("Data file created successfully.\n");

    return 0;
}
