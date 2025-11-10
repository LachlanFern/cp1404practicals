"""
Project management program
Estimate: 120 mins
Actual:
"""

from project import Project
import datetime
filename = "projects.txt"

def main():
    menu = """(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd a new project
(U)pdate project
(Q)uit"""
    projects = load_projects()
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} from {filename}")
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_projects(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    final_choice = input(f"Would you like to save to {filename}? Y/N" ).upper()
    if final_choice == "Y":
        save_projects(projects)
    elif final_choice == "N":
        print("Thank you for using this project management software.")
    else:
        print("Please confirm your choice with 'Y' or 'N'")


def load_projects():
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split('\t')
        start_date_string = parts[1]
        start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
        project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects

def save_projects(projects):
    with open(filename, "w") as out_file:
        for project in projects:
            print(f"{project.name}, {project.start_date}, {project.priority}, {project.cost}, {project.completion}", file=out_file)
    print(f"{len(projects)} projects saved")

def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in incomplete:
        print(project)

    print("Completed projects:")
    for project in complete:
        print(project)

def update_projects(projects):
    for i, project in enumerate(projects):
        print(f"{i}: {project}")

    choice = int(input("Project choice: "))
    update_project = projects[choice]
    new_priority = input("New priority level: ")
    new_completion = input("New completion level:  ")

    update_project.update(new_priority, new_completion)

def add_projects(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    except ValueError:
        print("Incorrect format please retry")
    priority = int(input("priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, filter_date, priority, cost, completion))
    print("Project added!")

def filter_projects(projects):
    date = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    except ValueError:
        print("Incorrect format please retry")
        return
    filtered = [project for project in projects if project.start_date > filter_date]

    if filtered:
        for project in filtered:
            print(project)
    else:
        print("No projects after that date")


main()