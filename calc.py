from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ")

if operation == "add":
    print("Result:", add(num1, num2))
elif operation == "subtract":
    print("Result:", subtract(num1, num2))
elif operation == "multiply":
    print("Result:", multiply(num1, num2))
elif operation == "divide":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")
