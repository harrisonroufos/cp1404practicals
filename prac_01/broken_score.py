"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    result = "Invalid score"
elif score < 50:
    result = "Bad"
elif score < 90:
    result = "Passable"
else:
    result = "Excellent"

print(result)