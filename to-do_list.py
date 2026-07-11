# Program: To-Do List

# Creating an empty to-do list
todo_list = []

# Taking the number of tasks from the user
number_of_tasks = int(input("Enter the number of tasks: "))

# Adding tasks to the list
for i in range(number_of_tasks):
    task = input("Enter task: ")
    todo_list.append(task)

# Displaying the current to-do list
print("\n----- To-Do List -----")

for task in todo_list:
    print(task)

# Removing a completed task
completed_task = input("\nEnter the completed task to remove: ")

if completed_task in todo_list:
    todo_list.remove(completed_task)
    print("\nTask removed successfully.")
else:
    print("\nTask not found.")

# Displaying the updated to-do list
print("\n----- Updated To-Do List -----")

for task in todo_list:
    print(task)
