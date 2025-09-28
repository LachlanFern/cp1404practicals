"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """This is the main function that gets an input or random number and prints the result"""

    #I don't know if I am supposed to keep the stuff below so I commented it out
    #score = float(input("Enter score: "))
    #result = score_result(score)
    #print(result)

    score = random.randint(0,100)
    result = score_result(score)
    print(result)


def score_result(score: float):
    """This function sorts the score into a result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()