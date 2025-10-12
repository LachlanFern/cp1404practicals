
def main():
    numbers = number_info()
    calculated = calculate_numbers(numbers)
    display_numbers(calculated)

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

main()