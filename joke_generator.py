# Program: Joke Generator

# Importing the random module
import random

# Creating a list of programming jokes
jokes = [
    "My keyboard and I had an argument.\nNow we're not on speaking terms.",

    "I renamed my dog 'Python'.\nNow everyone thinks I walk my code every morning.",

    "The computer looked at me.\nI looked at the computer.\nNeither of us knew why the code worked.",

    "My laptop blinked first.\nI won the staring contest.",

    "I whispered 'Hello World' to my computer.\nIt replied, 'I've heard that one before.'",

    "I asked ChatGPT to write my homework.\nIt asked me if I had tried turning my brain off and on again.",

    "My code and I have one thing in common.\nWe both work better after coffee.",

    "I told my computer a joke.\nNow it's still loading the punchline.",

    "My USB said, 'Try flipping me one more time.'",

    "I accidentally complimented my compiler.\nNow it's giving me positive errors."
]

# Displaying the title
print("----- Welcome to the Joke Generator! -----")

# Waiting for the user to continue
input("\nPress Enter to hear a programming joke...")

# Displaying a random joke
print("\nHere's your joke:\n")
print(random.choice(jokes))

print("\nThanks for stopping by! Come back for another joke.")
