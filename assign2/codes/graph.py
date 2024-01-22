import matplotlib.pyplot as plt
import numpy as np

# Function to calculate x(n)
def calculate_x(n):
    return (5/2) * (1/2)**n * (n >= 0)  # Multiply by the unit step function

# Generate values for n from -3 to 8
n_values = np.arange(-3, 9)

# Calculate x(n) for each n
x_values = calculate_x(n_values)

# Plotting
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-', label='x(n)')
plt.title('Plot of x(n) vs n',fontsize=16)
plt.xlabel('n',fontsize=16)
plt.ylabel('x(n)',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.legend(fontsize=16)
plt.savefig('stem plot.png', dpi=600)
plt.show()
