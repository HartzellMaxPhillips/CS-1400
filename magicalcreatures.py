print("We will need two numbers, the percentage of a population against the maximum population an area can sustatin \
as well as the rate of growth.  The population should be a number between 0 and 1.  The rate of growth should be a number between 0 and 4.  \
Make sure to round both the population and growth rate to 3 decimal places")

def three_decimal_places(num): #Function checking for 3 decimal places
    # Convert the float to a string
    num_str = str(num)
    
    # Split the string into integer and decimal parts
    integer_part, decimal_part = num_str.split(".")
    
    # Check if the decimal part has exactly three characters
    if len(decimal_part) <= 3:
        return True
    else:
        return False
    
def logistics_formula_application(population, population_growth):
    population_next = population_growth * population *(1 - population)
    population = population_next
    return population 

while True: #Validating correct starting population
    try:
        populationZero = input("Population? ")
        population = float(populationZero)
        if population != 0 < population < 1 and three_decimal_places(population):
            break
        else:
            print("Please pick a number that has the decimal rounded to 3 places and is between 0 and 1")
    except ValueError:
        print("Please input a correct number.")

while True: #Validating Correct growth rate
    try:
        growthRate = input("Growth Rate? ")
        population_growth = float(growthRate)
        if population_growth != 0 < population_growth < 4 and three_decimal_places(growthRate):
            break
        else:
            print("Please pick a number between 0 and 4 that is rounded to 3 decimal places")
    except ValueError:
        print("please input a correct number")

print(f"{population} Is the population percentage")
print(f"{population_growth} Is the growth rate")
population = logistics_formula_application(population, population_growth)
print("")
print (population)

