# Program: Shopping List

# Creating an empty shopping list
shopping_list = []

# Taking the number of items from the user
number_of_items = int(input("Enter the number of items: "))

# Adding items to the shopping list
for i in range(number_of_items):
    item = input("Enter item: ")
    shopping_list.append(item)

# Displaying the shopping list
print("\n----- Shopping List -----")

for item in shopping_list:
    print(item)
