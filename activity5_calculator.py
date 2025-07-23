num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)  # Addition
elif operation == "-":
    print(num1 - num2)  # Subtraction
elif operation == "*":
    print(num1 * num2)  # Multiplication
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)  # Division
    else:
        print("Error: Division by zero")  # Error case
else:
    print("Invalid operation")  # Wrong operator