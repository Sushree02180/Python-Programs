# Program: Age Calculator

# Importing the datetime module
import datetime

# Taking the birth year from the user
birth_year = int(input("Enter your birth year: "))

# Getting the current year
current_year = datetime.datetime.now().year

# Calculating the age
age = current_year - birth_year

# Displaying the result
print("Your age is:", age, "years.")
