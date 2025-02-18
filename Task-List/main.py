from task import Task


def main_menu(tasklist):
    """displays the main menu and returns the user’s valid input"""

    # Displaying the title and options for main menu
    print("-Tasklist-")
    print(f"You have {len(tasklist)} tasks.")
    print("1. Display current task")
    print("2. Mark current task complete")
    print("3. Postpone current task")
    print("4. Add new task")
    print("5. Save and quit")
    while True:
        choice = input("Enter choice: ")
        # Checking for a valid input
        if choice in {'1', '2', '3', '4', '5'}:
            return int(choice)
        else:
            print("Invalid choice. Please choose again.")


def read_file():
    """ Constructing a task object from each line and adding it to a list"""
    try:
        # Opening the tasklist.txt file for reading the content in it
        with open('tasklist.txt', 'r') as file:
            tasks = []
            # Adding the description, date and time to the list
            for line in file:
                description, date, time = line.strip().split(',')
                tasks.append(Task(description, date, time))
            # Sort tasks after reading from file
            tasks.sort()
            return tasks
    # Return an empty list if file does not exist
    except FileNotFoundError:
        return []


def write_file(tasklist):
    """passes in the list of tasks that will be written to the file (‘tasklist.txt’)"""

    # Opening the tasklist.txt file for writing over the existing content
    with open('tasklist.txt', 'w') as file:
        for task in tasklist:
            # Writing each task to the file
            file.write(repr(task) + '\n')


def get_date():
    """prompts the user to enter the month, day, and year"""
    while True:
        try:
            # Getting the month, day, and year
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            year = int(input("Enter year: "))
            # Validating the input
            if 1 <= month <= 12 and 1 <= day <= 31 and 2000 <= year <= 2100:
                return f"{month:02}/{day:02}/{year}"
            # Prompting the user for a valid date
            else:
                print("Invalid date. Please enter a valid date.")
        # Handling error input
        except ValueError:
            print("Invalid input. Please enter numeric values for month, day, and year.")


def get_time():
    """prompts the user to enter the hour and minute"""
    while True:
        try:
            # Getting the hour and minute
            hour = int(input("Enter hour: "))
            minute = int(input("Enter minute: "))
            # Validating the input
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                return f"{hour:02}:{minute:02}"
            # Prompting the user for a valid time
            else:
                print("Invalid time. Please enter a valid time.")
        # Handling error input
        except ValueError:
            print("Invalid input. Please enter numeric values for hour and minute.")


def main():
    tasklist = read_file()

    while True:
        # Showing the menu and getting the user's choice
        choice = main_menu(tasklist)

        # Option 1: Display the current task
        if choice == 1:
            if tasklist:
                print("Current task is:")
                print(tasklist[0])
            else:
                print("All tasks are complete.")

        # Option 2: Mark current task as complete
        elif choice == 2:
            if tasklist:
                print("Marking current task complete:")
                print(tasklist.pop(0))
                if tasklist:
                    print("New current task is:")
                    print(tasklist[0])
                else:
                    print("All tasks are complete.")
            else:
                print("All tasks are complete.")

        # Option 3: Postpone current task
        elif choice == 3:
            if tasklist:
                print("Postponing current task:")
                task = tasklist.pop(0)
                print(task)
                new_date = get_date()
                new_time = get_time()
                postponed_task = Task(task.get_description(), new_date, new_time)
                tasklist.append(postponed_task)
                tasklist.sort()
            else:
                print("All tasks are complete.")

        # Option 4: Add new task
        elif choice == 4:
            description = input("Enter a task: ")
            date = get_date()
            time = get_time()
            new_task = Task(description, date, time)
            tasklist.append(new_task)
            tasklist.sort()

        # Option 5: Save and quit
        elif choice == 5:
            write_file(tasklist)
            print("Tasks saved. Exiting program.")
            break


if __name__ == "__main__":
    main()
