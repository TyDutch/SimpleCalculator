def operation():
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Enter Valid Input")
    while True:
        operator = input("Enter the operation you'd like to calculate: ")
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            break
        elif operator != '+' or operator != '-' or operator != '*' or operator != '/':
            print(f"Invalid Operator: {operator}")
    while True:
        try:
            second_number = float(input("Enter the second number: "))
            if operator == '+':
                return first_number + second_number
            elif operator == '-':
                return first_number - second_number
            elif operator == '*':
                return first_number * second_number
            elif operator == '/':
                return first_number / second_number 
        except ValueError:
            print("Enter Valid Second Number")

print(operation())