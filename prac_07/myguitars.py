from prac_07.guitar import Guitar

filename = "guitars.csv"

def main():
    menu ="""(D)isplay guitars
(A)dd a new guitar
(S)ave guitars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    guitars = load_guitars()
    while choice != "Q":
        if choice == "D":
            display_guitars(guitars)
        elif choice == "A":
            add_guitar(guitars)
        elif choice == "S":
            save_guitars(guitars)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("goodbye")

def load_guitars():
    """Loads guitars from file and creates list"""
    guitars = []
    in_file = open(filename, 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), parts[2])
        guitars.append(guitar)
    in_file.close()
    return guitars

def add_guitar(guitars):
    """Add new guitar to list"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

def display_guitars(guitars):
    """Display list of guitars"""
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def save_guitars(guitars):
    """Save list of guitars"""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    print(f"{len(guitars)} guitars saved")

main()

