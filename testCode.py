while True:
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

print("You entered:", float_value)


'''test_number = 2.3234
if three_decimal_places(test_number):
    print("correct decimal")
else:
    print("incorrect deciaml")'''