"""
CP1404 Practical
"""
import random

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBERS_PER_LINE = 6


def main():
    numbers = generate_quick_pick_numbers(MIN_NUMBER, MAX_NUMBER, NUMBERS_PER_LINE)
    print(numbers)


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
