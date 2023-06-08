"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Determine given score grade category"""
    score = float(input("Enter score: "))
    result = determine_score_category(score)
    print(result)
    print(determine_score_category(random.randint(0, 100)))


def determine_score_category(score):
    """Determines score category"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
