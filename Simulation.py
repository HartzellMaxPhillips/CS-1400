import sys

def get_input(): #Acquires the input from the console.

    population = float(sys.argv[1])
    population_growth = float(sys.argv[2])
    generations = int(sys.argv[3])
    output_file = sys.argv[4]

    return population, population_growth, generations, output_file

def creature_growth_simulation (population: float, population_growth: float, generations: int, output_file: str ): #Main function that holds the simulation
    
    if False != 0 < population < 1 and 0 < population_growth < 4: #checking for valid numbers
        print("Incorrect inputs")
        exit()
    
    def logistics_formula_application(population, population_growth): #Applying the logistics formula
        population_next = population_growth * population *(1 - population)
        population = population_next
        return population 

    population_list = [] # initializing lists

    i = 1
    for list_population in range(generations + 3): #Populating list
        population_list.append(population)
        population = logistics_formula_application(population, population_growth)
        i += 1

    
    with open(output_file, "w") as data_file: #Oupting list to data file
        for index, value in enumerate(population_list):
            data_file.write(f'{index}   ')
            data_file.write(f'{value:.3f}\n')


    
population, population_growth, generations, output_file = get_input() #actually performing the actions within the simulation with these two lines.
creature_growth_simulation(population, population_growth, generations, output_file)

'''lst = ["a","b","c","d","e","f","g"]
for index, value in enumerate(lst):
    print("index: ", index, "value: ", value)'''

'''    j = 1
    while j < generations + 2: #outputing list contents
        x = population_list.pop(0)
        y = time.pop(0)
        print(y, end="  ")
        print(f'{x:.3f}')
        j += 1
'''