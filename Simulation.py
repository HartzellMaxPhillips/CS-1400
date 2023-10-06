def get_user_input():
    user_input = input("Enter four variables separated by spaces: ")
    population, population_growth, generations, output_file = map(str.strip, user_input.split(' '))

    return population, population_growth, generations, output_file



def creature_growth_simulation (population: float, population_growth: float ): #, generations: int, output_file
        
    def logistics_formula_application(population, population_growth):
        population_next = population_growth * population *(1 - population)
        population = population_next
        return population 

    population, population_growth, generations, output_file = get_user_input()
    creature_growth_simulation (population, population_growth, generations, output_file)

    population_list = []
    time = []
    print(population)
    population = logistics_formula_application(population, population_growth)
    print(population)
    



