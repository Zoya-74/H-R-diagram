import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('Cluster_data - Sheet1.csv')  

# Extract relevant columns
temperature = df['Temperature (K)']
luminosity = df['Luminosity(Solar)']


# Create HR diagram
plt.figure(figsize=(10, 6))
plt.scatter(temperature, luminosity, c='seagreen', marker='o', s=10, label='Stars')

# Customize plot
plt.title('Hertzsprung-Russell Diagram')
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (Watts)')
plt.xscale('log')  
plt.yscale('log')  
plt.gca().invert_xaxis()  # Reverse the temperature axis 

# Add grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()
