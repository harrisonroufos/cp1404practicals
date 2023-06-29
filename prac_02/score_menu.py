"""Score menu"""

MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Menu that gets score and determine result and print score in stars"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_category(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """ Get valid score """
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


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


def print_stars(password):
    """Print stars"""
    print("*" * password)


main()
