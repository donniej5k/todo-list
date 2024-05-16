#The Todo list project:

from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority, due_date):
        self.tasks.append({'title': title, 'status': 'Incomplete', 'priority': priority, 'due_date': due_date})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = task['status']
                color = "\033[92m" if status == "Complete" else "\033[91m"
                print(f"{index}. {task['title']} - {status} - Priority: {task['priority']} - Due: {task['due_date']} {color}")

    def mark_task_complete(self, task_number):
        try:
            self.tasks[task_number - 1]['status'] = 'Complete'
            print("Task marked as complete.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print("Task deleted.")
        except IndexError:
            print("Invalid task number.")

def display_menu():
    print("""
Welcome to the To-Do List App!

    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

def main():
    todo_list = ToDoList()
    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                title = input("Enter the task title: ")
                priority = input("Enter the task priority (Low, Medium, High): ")
                due_date = input("Enter the due date (YYYY-MM-DD): ")
                todo_list.add_task(title, priority, due_date)
                print("Task added.")
            elif choice == 2:
                todo_list.view_tasks()
            elif choice == 3:
                task_number = int(input("Enter the task number to mark as complete: "))
                todo_list.mark_task_complete(task_number)
            elif choice == 4:
                task_number = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_number)
            elif choice == 5:
                print("Quitting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Returning to the main menu...\n")

if __name__ == "__main__":
    main()
