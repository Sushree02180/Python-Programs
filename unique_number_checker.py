# Program: Unique Number Checker

# Creating an empty set
unique_numbers = set()

# Taking the number of elements from the user
count = int(input("Enter the number of elements: "))

# Adding numbers to the set
for i in range(count):
    number = int(input("Enter a number: "))
    unique_numbers.add(number)

# Displaying the unique numbers
print("\n----- Unique Numbers -----")

for number in unique_numbers:
    print(number)
