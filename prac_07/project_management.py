import datetime
from project import Project
from operator import attrgetter
MENU = """Menu:
(L)oad Projects
(S)ave Projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate new project
(Q)uit
"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            isvalid = False
            while not isvalid:
                try:
                    filename = input("Filename:")
                    if filename == "":
                        print("Invalid input; enter a valid filename")
                    else:
                        with open(filename, "r") as in_file:
                            in_file.readline()
                            projects = []
                            for line in in_file:
                                parts = (line.strip('\n').split('\t'))
                                start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                                project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
                                projects.append(project)
                        isvalid = True
                except ValueError:
                    print("Invalid input; enter a valid filename")
        elif choice == "S":
            filename = input("Filename: ")
            with open(filename, "w") as out_file:
                print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
                for project in projects:
                    print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                          f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
        elif choice == "D":
            print("Incomplete projects: ")
            incomplete_project = [project for project in projects if not project.is_completed()]
            incomplete_project.sort()
            for project in incomplete_project:
                date_to_string(project)
                print(' ', project)
            print("Completed projects: ")
            completed_projects = [project for project in projects if project.is_completed()]
            completed_projects.sort()
            for project in completed_projects:
                date_to_string(project)
                print(' ', project)
        elif choice == "F":
            date_filter = input("Show projects that start after this date (dd/mm/yyyy): ")
            date = string_to_date(date_filter)
            project_filter = [project for project in projects if project.start_date >= date_filter]
            project_filter.sort(key=attrgetter("start_date"))
            for project in project_filter:
                date_to_string(project)
                if string_to_date(project.start_date) >= date:
                    print(project)
        elif choice == "A":
            print("Lets add a new project")
            new_project_name = input("Name: ")
            new_start_date = input("Start date (dd/mm/yy): ")
            new_priority = int(input("Priority: "))
            new_cost_estimate = float(input("Cost estimate: $"))
            new_completion_percentage = int(input("Percent complete: "))
            new_project = Project(new_project_name, new_start_date, new_priority,
                                  new_cost_estimate, new_completion_percentage)
            projects.append(new_project)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            index = int(input("Project choice: "))
            update_project = projects[index]
            print(update_project)
            try:
                completion_percentage = int(input("New percentage: "))
                update_project.completion_percentage = completion_percentage
            except ValueError:
                pass
            try:
                priority = int(input("New Priority: "))
                update_project.priority = priority
            except ValueError:
                pass
        else:
            print("Invalid Menu choice")
        print(MENU)
        choice = input(">>> ").upper()


def date_to_string(project):
    if not isinstance(project.start_date, str):
        project.start_date = project.start_date.strftime("%d/%m/%Y")

def string_to_date(date_filter):
    return datetime.datetime.strptime(date_filter, "%d/%m/%Y").date()
main()