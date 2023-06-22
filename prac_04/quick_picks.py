"""
CP1404 Practical
"""
import random
from operator import itemgetter

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBERS_PER_LINE = 6


def main():
    """Prints quick picks numbers in ascending order"""
    numbers = []
    number_of_picks = int(input("How many quick picks? "))
    for pick in range(number_of_picks):
        numbers.append(generate_quick_pick_numbers(MIN_NUMBER, MAX_NUMBER, NUMBERS_PER_LINE))
    numbers.sort(key=itemgetter(-1))
    for number in numbers:
        for part in number:
            print(f"{part:2}", end=" ")
        print("")


def generate_quick_pick_numbers(min_number, max_number, number_of_numbers):
    """Generate list of set amount random numbers between min and max with no duplicates"""
    numbers = []
    for number in range(number_of_numbers):
        random_number = random.randint(min_number, max_number)
        while random_number in numbers:
            random_number = random.randint(min_number, max_number)
        numbers.append(random_number)
    numbers.sort()
    return numbers


main()
