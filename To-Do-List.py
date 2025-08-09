import datetime

# List to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("\n📭 No tasks in the list.\n")
        return
    print("\n📝 To-Do List:")
    print(f"{'S.No':<6}{'Time Added':<20}{'Task'}")
    print("-" * 50)
    for i, task in enumerate(tasks, start=1):
        print(f"{i:<6}{task['time']:<20}{task['description']}")
    print()

# Function to add a task
def add_task():
    desc = input("Enter the task: ")
    time_added = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"time": time_added, "description": desc})
    print("✅ Task added successfully.\n")

# Function to update a task
def update_task():
    display_tasks()
    try:
        task_num = int(input("Enter the serial number of the task to update: "))
        if 1 <= task_num <= len(tasks):
            new_desc = input("Enter the new description: ")
            tasks[task_num - 1]['description'] = new_desc
            print("🔄 Task updated successfully.\n")
        else:
            print("❌ Invalid serial number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Function to delete a task
def delete_task():
    display_tasks()
    try:
        task_num = int(input("Enter the serial number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("🗑️ Task deleted successfully.\n")
        else:
            print("❌ Invalid serial number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Main loop
def main():
    while True:
        print("📋 To-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
