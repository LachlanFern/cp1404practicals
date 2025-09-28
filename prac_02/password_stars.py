

def main():
    """This function runs the other functions"""
    password= get_password()
    print_password(password)


def get_password() -> str:
    """This function checks if the inputted password is valid"""
    password = input("Please enter password: ")
    min_length=5

    while len(password) < min_length:
        print("Please input a password longer than 5 characters")
        password = input("Please enter password: ")

    return password

def print_password(password: str):
    """This function prints stars to the length of the password"""
    print("*" * len(password))


main()