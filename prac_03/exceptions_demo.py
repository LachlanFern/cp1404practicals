"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the input isn't an integer or not a number
2. When will a ZeroDivisionError occur? when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? by adding an if statement to the denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
