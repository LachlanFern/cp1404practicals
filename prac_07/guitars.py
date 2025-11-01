from prac_07.guitar import Guitar

filename = "guitars.csv"

def main():
    guitars = []
    in_file = open(filename, 'r')
    in_file.readline()


    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), parts[2])
        guitars.append(guitar)
    in_file.close()

    guitars.sort()
    for guitar in guitars:
        print(guitar)
main()

