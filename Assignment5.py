# Task Management using local Storage

import os


class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __str__(self):
        return f"Title: {self.title}, Description: {self.desc}"

    @staticmethod
    def from_string(task_str):
        title, desc = task_str.strip().split(', ')
        return Task(title.split(": ")[1], desc.split(": ")[1])


# Save tasks to a file
def save_tasks_to_file(tlist, filename="tasks.txt"):
    try:
        with open(filename, "w") as file:
            for task in tlist:
                file.write(str(task) + "\n")
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")


# Load tasks from a file
def load_tasks_from_file(filename="tasks.txt"):
    tlist = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    task = Task.from_string(line)
                    tlist.append(task)
            print("Tasks loaded successfully!")
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")
    return tlist


# Create new Task
def create_task(tlist, title, desc):
    t = Task(title, desc)
    tlist.append(t)
    save_tasks_to_file(tlist)  # Save the updated task list to file
    print(title, "Created Successfully")


# Read
def read_task(tlist):
    if not tlist:
        print("No tasks")
    else:
        for t in tlist:
            print(t)


# Update
def update_task(tlist, title, newdesc=None):
    for i in tlist:
        if i.title == title:
            if newdesc:
                i.desc = newdesc
                save_tasks_to_file(tlist)  # Save the updated task list to file
                print("Task Updated Successfully")
                return
    print("Task Not Found")


# Delete
def delete_task(tlist, title):
    for task in tlist:
        if task.title == title:
            tlist.remove(task)
            save_tasks_to_file(tlist)  # Save the updated task list to file
            print("Task deleted Successfully")
            return
    print("Task doesn't exist")


def main():
    tlist = load_tasks_from_file()  # Load existing tasks from file

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        a = int(input("Choose the option: "))

        if a == 1:
            title = input("Enter the Title: ")
            desc = input("Enter the description: ")
            create_task(tlist, title, desc)

        elif a == 2:
            read_task(tlist)

        elif a == 3:
            title = input("Enter the title: ")
            newdesc = input("Enter the new description: ")
            update_task(tlist, title, newdesc)

        elif a == 4:
            title = input("Enter the title of the task to delete: ")
            delete_task(tlist, title)

        elif a == 5:
            print("Exiting Task Manager")
            break

        else:
            print("Enter a valid option")


if __name__ == '__main__':
    main()

