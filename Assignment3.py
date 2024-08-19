# CRUD application

class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __str__(self):
        return f"Title: {self.title}, Description: {self.desc}"

# Create new Task
def create_task(tlist, title, desc):
    t = Task(title, desc)
    print(t)
    tlist.append(t)
    print(title,"Created Successfully")

# Read
def read_task(tlist):
    if not tlist:
        print("No tasks")
    else:
        for t in tlist:
            print(t)

# Update
def update_task(tlist, title, newdesc= None):
    for i in tlist:
        if i.title == title:
            if newdesc:
                i.desc = newdesc
                print("Task Updated Successfully")
                return
    print("Task Not Found")

def delete_task(tlist, title):
    for task in tlist:
        if task.title == title:
            tlist.remove(task)
            print("Task deleted Successfully")
            return
    print("Task doesnt exist")


def main():
    tlist = []
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        a = int(input("Choose the option :"))

        if a == 1:
            title = input("Enter the Title: ")
            desc = input("Enter the description: ")
            create_task(tlist,title,desc)

        elif a == 2:
            read_task(tlist)

        elif a == 3:
            title = input("Enter the title: ")
            newdesc = input("Enter the new description: ")
            update_task(tlist,title,newdesc)

        elif a == 4:
            title = input("Enter the title of the task to delete: ")
            delete_task(tlist,title)

        elif a == 5:
            print("Exiting Task Manager")
            break

        else:
            print("Enter valid option")

if __name__ == '__main__':
    main()







