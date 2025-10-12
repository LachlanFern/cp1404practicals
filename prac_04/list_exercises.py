
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    numbers = number_info()
    calculated = calculate_numbers(numbers)
    display_numbers(calculated)

    user_input = ask_username()
    check_username(user_input)

def number_info():
    """Get 5 numbers from the user"""
    numbers =[]
    while len(numbers) < 5:
        num_input = float(input("Please enter 5 numbers: "))
        numbers.append(num_input)
    return numbers


def calculate_numbers(numbers):
    """Calculate first, last, smallest, largest and average"""
    first_num = numbers[0]
    last_num = numbers[-1]
    small_num = min(numbers)
    big_num = max(numbers)
    avg_num = sum(numbers) / len(numbers)
    return avg_num, big_num, first_num, last_num, small_num

def display_numbers(calculated):
    """Display results"""
    avg_num, big_num, first_num, last_num, small_num = calculated
    print(f"The first number is {first_num}")
    print(f"The last number is {last_num}")
    print(f"The smallest number is {small_num}")
    print(f"The largest number is {big_num}")
    print(f"The average of the numbers is {avg_num}")

def ask_username():
    """Get username from the user"""
    user_input = input("please enter username: ")
    return user_input
def check_username(user_input):
    """Check if username is on the list"""
    if user_input in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

main()