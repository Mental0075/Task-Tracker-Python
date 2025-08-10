import datetime
import random
import json
import os

all_task = []
task_file_name = 'task_tracker.json'

class Task:
    def addTask(self, description):
        self.description = description
        self.status = 'Todo'
        self.created_datetime = self.get_current_datetime()
        self.last_modified_datetime = self.get_current_datetime()
        self.id = self.get_unique_number()

    def print_task(self):
        print(f'Id : {self.id}')
        print(f'Description : {self.description}')
        print(f'Status : {self.status}')
        print(f'Created DateTime : {self.created_datetime}')
        print(f'Last Modified DateTime : {self.last_modified_datetime}')

    def get_current_datetime(self):
        return datetime.datetime.now()

    def get_unique_number(self):
        list_size = len(all_task)
        new_task_number = list_size + random.randint(1, 1000)
        return f"TASK-{new_task_number:05d}"

    def get_dict(self):
        return {
            'Id': self.id,
            'Description': self.description,
            'Status': self.status,
            'Created DateTime': str(self.created_datetime),
            'Last Modified DateTime': str(self.last_modified_datetime),
        }

    def get_json(self):
        return json.dumps(self.get_dict(), indent=4)

    @staticmethod
    def load_tasks_from_json():
        if not os.path.exists(task_file_name):
            return
        
        with open(task_file_name, 'r') as file:
            try:
                data = json.load(file)
                for task_dict in data:
                    new_task = Task()
                    new_task.id = task_dict['Id']
                    new_task.description = task_dict['Description']
                    new_task.status = task_dict['Status']
                    # You might need to convert the datetime string back to a datetime object here
                    new_task.created_datetime = task_dict['Created DateTime']
                    new_task.last_modified_datetime = task_dict['Last Modified DateTime']
                    all_task.append(new_task)
            except json.JSONDecodeError:
                print("JSON file is empty or corrupted.")
            except KeyError as e:
                print(f"Key error while loading task: {e}")


def display_menu():
    print("\n--- Task Manager Menu ---")
    print("1. Add New Task")
    print("2. Start Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. All Task")
    print("6. All Todo Task")
    print("7. All In Progress Task")
    print("8. All Completed Task")
    print("9. Exit")
    print("----------------------------")

# Main functions for user interaction
def add_new_task_action():
    do_validation = True
    while do_validation:
        description = input("Enter task name: ")
        print(len(description.strip()))
        if len(description.strip()) == 0:
            print('I am in If ')
            print('Please enter valid task name.')
        else:
            print('I am in else ')
            do_validation = False
    if not do_validation:
        new_task = Task()
        new_task.addTask(description)
        all_task.append(new_task)
        save_tasks_to_file()
        print(f"Task '{description}' added successfully with ID {new_task.id}.")

def update_task_status_action(status):
    task_id = input(f"Enter the ID of the task to set to '{status}': ")
    for task in all_task:
        if task.id == task_id:
            task.status = status
            task.last_modified_datetime = task.get_current_datetime()
            print(f"Task '{task_id}' status updated to '{status}'.")
            save_tasks_to_file()
            return
    print(f"Error: Task with ID '{task_id}' not found.")

def delete_task_action():
    task_id = input("Enter the ID of the task to delete: ")
    # Iterate over a copy of the list to avoid modifying it while looping
    for task in all_task[:]:
        if task.id == task_id:
            all_task.remove(task)
            print(f"Task with ID '{task_id}' deleted successfully.")
            save_tasks_to_file()
            return
    print(f"Error: Task with ID '{task_id}' not found.")

def display_tasks_by_status(status):
    print(f"\n--- Tasks with status '{status if status else 'All'}' ---")
    tasks_to_display = all_task if status == '' else [t for t in all_task if t.status == status]
    if not tasks_to_display:
        print("No tasks found.")
        return

    for task in tasks_to_display:
        task.print_task()
        print("-" * 20)

def save_tasks_to_file():
    list_of_dicts = [task.get_dict() for task in all_task]
    with open(task_file_name, 'w') as file:
        json.dump(list_of_dicts, file, indent=4)


def main():
    # Load tasks from file at the start of the program
    Task.load_tasks_from_json()

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            add_new_task_action()
        elif choice == '2':
            update_task_status_action('In Progress')
        elif choice == '3':
            update_task_status_action('Completed')
        elif choice == '4':
            delete_task_action()
        elif choice == '5':
            display_tasks_by_status('') # All tasks
        elif choice == '6':
            display_tasks_by_status('Todo')
        elif choice == '7':
            display_tasks_by_status('In Progress')
        elif choice == '8':
            display_tasks_by_status('Completed')
        elif choice == '9':
            print('Thank You')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 9.')


if __name__ == "__main__":
    main()