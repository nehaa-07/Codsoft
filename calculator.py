#task 2
#Creating a function of calculator
def calculator():
    print("Welcome to the Simple Calculator!")

#function to take input of first number from the user 
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

#function to take input of second number from the user 
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

#user input to select the operation to be performed
    print("\nChoose the operation:")
    print(" + for addition")
    print(" - for subtraction")
    print(" * for multiplication")
    print(" / for division")

    operation = input("Enter operation: ")

#performing the selected operation
    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation selected.")

# Using the calculator
calculator()
