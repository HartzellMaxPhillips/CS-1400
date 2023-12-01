
'''
Project: Random walk
Author: Hartzell Max Phillips
Date: 12/1/2023

'''

import random
import matplotlib.pyplot as plt
#def main()
###### DO NOT change this function #####
# Function to plot the random walk for each animal
def plot_walk(animal):
    xs, ys = zip(*animal['positions'])

    plt.figure(figsize=(10,10))
    plt.scatter(xs, ys, color=animal['color'], edgecolor='k', alpha=0.7, s=100, marker=animal['marker'])
    plt.plot(xs, ys, lw=1.5, ls='--', color=animal['color'])
    plt.grid(True)
    plt.title(f'Path of Random Walk for {animal["name"]}')
    plt.xlabel('East-West')
    plt.ylabel('North-South')
    
    # Save the plot to a file
    plt.savefig(f'{animal["name"]}_random_walk.png', dpi=300)
    #plt.close()  # Close the figure

# You need to create the animal dictionary inside the main function where each animal has
# direction, probabilities, positions, marker and color attributes
animal = {}

def simulate_chuck():
    chuck = { 'name' : 'chuck', 'color' : 'blue', 'marker' : 'o', 'positions' : [(0,0)], }

    for _ in range(1000):
        direction =  random.randrange(1, 101)
        if 0 <= direction <= 25:
            chuck['positions'].append((chuck['positions'][-1][0], chuck['positions'][-1][1] + 1))
        elif 26 <= direction <= 50:
            chuck['positions'].append((chuck['positions'][-1][0], chuck['positions'][-1][1] - 1))
        elif 51 <= direction <= 75:
            chuck['positions'].append((chuck['positions'][-1][0] + 1, chuck['positions'][-1][1]))
        elif 76 <= direction <= 100:
            chuck['positions'].append((chuck['positions'][-1][0] - 1, chuck['positions'][-1][1]))
    
    plot_walk(chuck)

def simulate_daisy():
    daisy = { 'name' : 'Daisy', 'color' : 'red', 'marker' : 's', 'positions' : [(0,0)], }

    for _ in range(1000):
        direction =  random.randrange(1, 101)
        if 0 <= direction <= 50:
            daisy['positions'].append((daisy['positions'][-1][0], daisy['positions'][-1][1] + 1))
        elif 51 <= direction <= 100:
            direction = random.randrange(1,4)
            if direction == 1:
                daisy['positions'].append((daisy['positions'][-1][0], daisy['positions'][-1][1] - 1))
            elif direction == 2:
                daisy['positions'].append((daisy['positions'][-1][0] + 1, daisy['positions'][-1][1]))
            elif direction == 3:
                daisy['positions'].append((daisy['positions'][-1][0] - 1, daisy['positions'][-1][1]))
    
    plot_walk(daisy)

def simulate_chester():
    chester = {'name' : 'Chester', 'color' : 'green', 'marker' : '^', 'positions' : [(0,0)], }

    for _ in range(1000):
        direction = random.randrange(1, 3)
        if direction == 1:
            chester['positions'].append((chester['positions'][-1][0] + 1, chester['positions'][-1][1]))
        elif direction == 2:
            chester['positions'].append((chester['positions'][-1][0] -1, chester['positions'][-1][1]))
    
    plot_walk(chester)

simulate_chuck()
simulate_daisy()
simulate_chester()
plt.show()