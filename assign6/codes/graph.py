import numpy as np
import matplotlib.pyplot as plt

# Load data from the generated data file
data = np.loadtxt('steady_state_errors.dat')
Ki_values = data[:, 0]
original_errors = data[:, 1]
adjusted_errors = data[:, 2]

# Plotting
#plt.figure(figsize=(10, 6))
plt.plot(Ki_values, original_errors, label='Original PID Gains')
plt.plot(Ki_values, adjusted_errors, label='Adjusted PID Gains')
plt.xlabel('Integral Gain (Ki)')
plt.ylabel('Steady-State Error')
#plt.title('Steady-State Error vs. Integral Gain (Ki)')
plt.legend()
plt.grid(True)
plt.savefig('steady_state_error.png')
