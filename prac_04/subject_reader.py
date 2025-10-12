"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_data(subjects)




def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_list = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject_list.append(parts)
    print(subject_list)
    return(subject_list)
    input_file.close()

def display_data(subjects):
    for line in subjects:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} number of students")


main()
