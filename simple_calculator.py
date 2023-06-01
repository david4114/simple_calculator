def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Error input! you need to choose an operation from the list, please try again.")


while True:
    while True:
        try:
            num_1 = float(input("Enter the first number: "))
            num_2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Error: Invalid input. You can only use numbers.")

    valid_operations = ['+', '-', '*', '/']

    while True:
        operation = input("Select an operation (+, -, *, /): ")
        if operation in valid_operations:
            break
        else:
            print("Error: Invalid input. You need to choose an operation from the list, please try again.")

    result = calculate(num_1, num_2, operation)
    print("The result is:", result)

    while True:
        choice = input("Would you like to perform another calculation? (yes/no): ")
        if choice.lower() == "no":
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice.lower() == "yes":
            break
        else:
            print("Error: Invalid input. Please enter 'yes' or 'no'.")

    if choice.lower() == "no":
        break

    #  I finish the code