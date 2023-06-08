"""Password stars"""
MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_valid_password()
    print_stars(len(password))


def get_valid_password():
    """Get valid password"""
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("To short.")
        password = input("Password: ")
    return password


def print_stars(length):
    print("*" * length)


main()
