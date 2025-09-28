

def main():
    menu="""(G)et a score between 0 and 100
(P)rint result
(S)how stars
(Q)uit"""
    score = None
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = int(input("Please enter your score: "))
        elif choice == "P":
            if score is None:
                print("No score entered")
            else:
                result = score_result(score)
                print(result)
        elif choice == "S":
            if score is None:
                print("No score entered!")
            elif score < 0 or score > 100:
                print("Invalid score can't show stars")
            else:
                print("*" * score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")

def score_result(score):
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

