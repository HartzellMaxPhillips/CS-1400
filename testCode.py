while True:
    try:
        user_input = input("Enter an integer: ")
        integer_value = int(user_input)
        break  # Break the loop if input is a valid integer
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("You entered:", integer_value)