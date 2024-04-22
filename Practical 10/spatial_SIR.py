#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 100  # Grid size
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
time_steps = 100  # Number of time steps to simulate
checkpoints = [0, 10, 50, 100]  # Time steps to plot

# Initialize the grid
population = np.zeros((N, N), dtype=int)
outbreak = np.random.choice(range(N), 2)  # Randomly choose the outbreak point
population[outbreak[0], outbreak[1]] = 1  # Set the outbreak point to 'infected'

# Prepare subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # 2x2 grid of subplots
axes = axes.ravel()  # Flatten axes array for easier iteration

def infect_neighbors(x, y, pop):
    """Infect the neighbors of an infected individual based on infection rate."""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # Skip the center point (the infected individual itself)
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:  # Ensure within bounds
                if pop[nx, ny] == 0:  # Susceptible
                    if np.random.random() < beta:
                        pop[nx, ny] = 1  # Infect

def recover_individuals(pop):
    """Recover infected individuals based on recovery rate."""
    infected_idx = np.where(pop == 1)
    for i in range(len(infected_idx[0])):
        if np.random.random() < gamma:
            pop[infected_idx[0][i], infected_idx[1][i]] = 2  # Recover
# step 0
ax = axes[0] 
ax.imshow(population, cmap='viridis', interpolation='nearest') 
ax.set_title('Time Step: 0') 
ax.axis('off')

# Simulation loop
for t in range(1, time_steps + 1):
    # Infect neighbors
    current_infected = np.where(population == 1)
    for i in range(len(current_infected[0])):
        infect_neighbors(current_infected[0][i], current_infected[1][i], population)
    
    # Recover individuals
    recover_individuals(population)

    # Save plots at specified checkpoints
    if t in checkpoints:
        ax = axes[checkpoints.index(t)]
        ax.imshow(population, cmap='viridis', interpolation='nearest')
        ax.set_title(f'Time Step: {t}') 
        ax.axis('off')

plt.tight_layout()
plt.show()