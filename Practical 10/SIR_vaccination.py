# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# parameter setting
N = 1000  # Total population
V = 0.1  # Not used necessarily
beta = 0.3  # The rate of infection
gamma = 0.05  # The rate of recovery
vaccination_rates = [i / 10 for i in range(11)]  

infected_dict = {}  

# Different vaccination rates
for v_rate in vaccination_rates:
    S = N - 1 - int(N * v_rate)  # Susceptible population 
    I = 1  # Initial number of infected individuals
    R = 0  # Initial number of recovered individuals

    I_arrays = [I]
    S_arrays = [S]
    R_arrays = [R]

    # Simulate over 1000 days
    for _ in range(1000):
        if S > 0:
            infect_prob = beta * I / N  # Infection probability
            new_infection = np.random.binomial(S, infect_prob)
        else:
            new_infection = 0

        if I > 0:
            new_recovery = np.random.binomial(I, gamma)
        else:
            new_recovery = 0
        
        # Update counts
        S -= new_infection
        I += new_infection - new_recovery
        R += new_recovery

        S = max(S, 0)  # Ensure S does not go below zero

        # Append the current state to arrays
        I_arrays.append(I)
        S_arrays.append(S)
        R_arrays.append(R)

    # Store the infection data for the current vaccination rate
    infected_dict[v_rate] = I_arrays

# Plotting the results
plt.figure(figsize=(6, 4), dpi=150)
for v_rate, I_arrays in infected_dict.items():
    plt.plot(I_arrays, label=f'Vaccination Rate: {v_rate * 100}%')

plt.xlabel('Time (days)')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.savefig("SIR_Vaccination_Model.png", format="png")  
plt.show()
plt.clf()  