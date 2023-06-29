"""Password stars"""
MINIMUM_PASSWORD_LENGTH = 8


def main():
    """Print password length in stars"""
    password = get_password()
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("To short.")
        password = input("Password: ")
    print_stars(len(password))


def get_password():
    """Get password"""
    password = input("Password: ")
    return password


def print_stars(password):
    """Print stars"""
    print("*" * password)


main()