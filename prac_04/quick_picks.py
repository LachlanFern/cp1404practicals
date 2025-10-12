import random


min_num = 1
max_num = 45
def main():

    num_quick_picks = int(input("How many quick picks?"))
    for i in range(num_quick_picks):
        quick_pick = create_quick_pick()
        quick_pick.sort()

        print(" ".join(f"{num:2}" for num in quick_pick))


def create_quick_pick():
    numbers =[]
    while len(numbers) < 6:
        num = random.randint(min_num,max_num)
        if num not in numbers:
            numbers.append(num)
    return numbers


main()