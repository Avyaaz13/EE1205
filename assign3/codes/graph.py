import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the coefficients of the polynomial
coefficients = [1, 2, 5, 80]

# Find the roots (zeros) and poles of the polynomial
zeros, poles, _ = signal.tf2zpk(coefficients, [1])

# Plot the pole-zero plot
plt.figure(figsize=(8, 6))
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Plot')
plt.legend()
plt.grid(True)
plt.savefig('poles_and_zeros_plot.png')
plt.show()

# Load data from the generated file
data = np.loadtxt('data.dat')
n_values = data[:, 0]
x_values = data[:, 1]

# Plot the graph
plt.figure(figsize=(8, 6))
plt.stem(n_values, x_values, label='x(n) vs n')
plt.xlabel('n', fontsize=14)
plt.ylabel('x(n)', fontsize=14)
plt.grid(True)
plt.legend(fontsize=14)
plt.title('x(n) vs n Plot')
plt.savefig('x_n_plot.png', dpi=600)
plt.show()
