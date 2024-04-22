# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define basic variables
N = 10000  # total population
I= 1    # initial number of infected individuals
S= N - I  # initial number of susceptible individuals
R = 0    # initial number of recovered individuals
beta = 0.3  # infection rate
gamma = 0.05  # recovery rate

# Create arrays to track variables over time
susceptible = [S]
infected = [I]
recovered = [R]

# Time course loop
for t in range(1000):
    if S > 0 and I > 0:
        # Calculate new infections and recoveries
        new_infections = np.random.binomial(S, beta * I / N)
        new_recoveries = np.random.binomial(I, gamma)

        # Update counts
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        # Store the updated counts
        susceptible.append(S)
        infected.append(I)
        recovered.append(R)
# Plotting
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(recovered, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')
plt.legend()
plt.savefig("SIR_Model.png", format="png") 
plt.show()

