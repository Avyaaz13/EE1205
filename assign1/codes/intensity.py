import numpy as np
import matplotlib.pyplot as plt

# Function for intensity
def intensity(r, lam):
    return np.cos(np.pi * r * lam)**2

# Range of r values
r_values = np.linspace(0, 2, 1000)

# Choose a value for lambda
lambda_value = 1

# Calculate intensity for each r
intensity_values = intensity(r_values, lambda_value)

# Plot the intensity
plt.plot(r_values, intensity_values, label=r'$\cos^2(\pi r)$')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Plot of Intensity vs r')
plt.legend()
plt.grid(True)
# Mark intensity values for r = 1 and r = 1/3
plt.scatter([1, 1/3], [intensity(1, lambda_value), intensity(1/3, lambda_value)], color='red')
plt.annotate('r = 1', xy=(1, intensity(1, lambda_value)), xytext=(1.25, intensity(1, lambda_value) + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('r = 1/3', xy=(1/3, intensity(1/3, lambda_value)), xytext=(0.5, intensity(1/3, lambda_value) - 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Save the plot
plt.savefig('intensity_plot.png')

# Show the plot
plt.show()
