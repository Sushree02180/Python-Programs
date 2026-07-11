# Program: Student Database

# Creating an empty dictionary
student = {}

# Taking input from the user
student["Name"] = input("Enter student name: ")
student["Age"] = int(input("Enter student age: "))
student["Course"] = input("Enter course name: ")

# Displaying the student details
print("\n----- Student Details -----")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])
