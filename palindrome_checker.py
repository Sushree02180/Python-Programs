# Program: Palindrome Checker

# Function to check whether a string is a palindrome
def check_palindrome(text):
    return text == text[::-1]

# Taking input from the user
text = input("Enter a string: ")

# Calling the function
if check_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
