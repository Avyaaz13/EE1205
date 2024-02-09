import numpy as np
import matplotlib.pyplot as plt

# Load data from the dat file
data = np.loadtxt('data4.dat')

# Separate n and y(n) values
n_values = data[:, 0]
y_values = data[:, 1]

# Plot the stem graph
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='y(n)')
highlight_n = 11
highlight_index = np.where(n_values == highlight_n)[0][0]
plt.stem(highlight_n, y_values[highlight_index], linefmt='red', markerfmt='o', basefmt='red',
         label=f'y({highlight_n}) = 234')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.savefig('y(n)plot.png')
plt.show()
