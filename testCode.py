import sys

x = len(sys.argv)
print(x)

'''while True:
    try:
        user_input = input("Enter an integer: ")
        integer_value = int(user_input)
        break  # Break the loop if input is a valid integer
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("You entered:", integer_value)

while True:
    try:
        user_input = input("Enter a float rounded to 2 decimals: ")
        float_value = round(float(user_input), 2)
        break  # Break the loop if input is a valid float rounded to 2 decimals
    except ValueError:
        print("Invalid input. Please enter a valid float rounded to 2 decimals.")

print("You entered:", float_value)'''

###
'''test_number = 2.3234
if three_decimal_places(test_number):
    print("correct decimal")
else:
    print("incorrect deciaml")'''

###
'''def three_decimal_places(num): #Function checking for 3 decimal places
        # Convert the float to a string
        num_str = str(num)
        
        # Split the string into integer and decimal parts
        integer_part, decimal_part = num_str.split(".")
        
        # Check if the decimal part has exactly three characters
        if len(decimal_part) <= 3:
            return True
        else:
            return False'''

###
'''print("We will need two numbers, the percentage of a population against the maximum population an area can sustatin \
as well as the rate of growth.  The population should be a number between 0 and 1.  The rate of growth should be a number between 0 and 4.  \
Make sure to round both the population and growth rate to 3 decimal places")
'''