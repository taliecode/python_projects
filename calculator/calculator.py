num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+ - * /): ")

while True:
    if operator == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Divide by zero!")
    else:
        print("Invalid")
    
    again = input("Next calculation? (y/n): ")
    if again != "y":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+ - * /): ")

print("Goodbye!")
