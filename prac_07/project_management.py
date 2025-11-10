"""
Project management program
Estimate: 120 mins
Actual:
"""

from project import Project
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
            break
            filter_projects(projects)
        elif choice == "A":
            break
            add_projects(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("goodbye")


def load_projects():
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
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



main()