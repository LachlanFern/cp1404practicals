password = input("Please enter password: ")
length = len(password)
while True:
    if length < 5:
        print("Please input a password longer than 5 characters")
        password = input("Please enter password: ")
        length = len(password)
    else:
        print("*" * length)
        break