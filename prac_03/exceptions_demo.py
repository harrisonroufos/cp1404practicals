"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When anything besides a integer has been entered.
2. When will a ZeroDivisionError occur?
When a zero has been inputted for a numerator/denominator in a division.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    while numerator == 0:
        print("Invalid")
        numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
