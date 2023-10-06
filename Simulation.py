import sys
#sys.argv.split()

def get_input():

    population = float(sys.argv[1])
    population_growth = float(sys.argv[2])
    generations = int(sys.argv[3])
    output_file = sys.argv[4]

    return population, population_growth, generations, output_file

def creature_growth_simulation (population: float, population_growth: float ): #, generations: int, output_file
        
    def logistics_formula_application(population, population_growth):
        population_next = population_growth * population *(1 - population)
        population = population_next
        return population 

    population_list = []
    time = []
    print(population)
    population = logistics_formula_application(population, population_growth)
    print(population)
    
population, population_growth, generations, output_file = get_input()
creature_growth_simulation(population, population_growth, ) #generations, output_file
