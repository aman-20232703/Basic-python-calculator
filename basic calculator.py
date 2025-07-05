# Welcome to the Python Basic Calculator
# This calculator performs addition, subtraction, multiplication, and division on two numbers.

import math

print("==========================================")
print(" Welcome to the Advanced Calculator App")
print("==========================================")

# Input: Get two numbers from the user
a = float(input("~~ Enter the 1st number: "))
b = float(input("~~ Enter the 2nd number: "))

# differents operations:-
print("\n~~Available operations~~")
print("1. Addition +")
print("2. Subtraction -")
print("3. Multiplication X")
print("4. Division /")
print("5. Power (a^b) ^")
print("6. Modulus (a % b) =")
print("7. Square Root **")
print("8. Average N/2")
print("9. Factorial N!")
print("0. Exit : ")

while True:
    choice = input("\nChoose an operation (0-9): ")
# exit from the calculation
    if choice == '0':
        print("Exiting the calculator. Thank you!")
        break
# Addition
    elif choice == '1':
        print(f"ADDITION: {a} + {b} = {a + b}")

# Subtraction
    elif choice == '2':
        print(f"SUBTRACTION: {a} - {b} = {a - b}")

# Multiplication
    elif choice == '3':
        print(f"MULTIPLICATION: {a} × {b} = {a * b}")

# Division (with zero check)
    elif choice == '4':
        if b != 0:
            print(f"DIVISION: {a} ÷ {b} = {a / b:.2f}")
        else:
            print("Division by zero is not allowed!")

# power
    elif choice == '5':
        print(f"POWER: {a}^{b} = {a ** b}")

# modulus
    elif choice == '6':
        print(f"MODULUS: {a} % {b} = {a % b}")

# sq.root
    elif choice == '7':
        print(f"SQ.ROOT: √{a} = {math.sqrt(a):.2f}")
        print(f"SQ.ROOT: √{b} = {math.sqrt(b):.2f}")

# avg.
    elif choice == '8':
        avg = (a + b) / 2
        print(f"Average of {a} and {b} = {avg}")

#  factorial
    elif choice == '9':
        if a >= 0 and a == int(a):
            print(f" Factorial of {int(a)} = {math.factorial(int(a))}")
        else:
            print(f"Factorial not defined for {a}")

        if b >= 0 and b == int(b):
            print(f"Factorial of {int(b)} = {math.factorial(int(b))}")
        else:
            print(f"Factorial not defined for {b}")

    else:
        print("Invalid choice! Please select from 0 to 9.")
