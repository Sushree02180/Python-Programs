# Program: Magic 8 Ball

# Importing the random module
import random

# Creating a list of positive responses
responses = [
    "Absolutely! Go for it!",
    "Believe in yourself—you've got this!",
    "The future looks bright for you.",
    "Without a doubt!",
    "Success is waiting just around the corner.",
    "Keep going! Great things take time.",
    "Every step you take brings you closer to your goal.",
    "Today is your lucky day!",
    "Trust yourself. Amazing things are ahead!",
    "Yes! I believe in you!",
    "Your hard work will pay off.",
    "Keep smiling—something wonderful is coming your way.",
    "Dream big and never give up.",
    "The answer is yes... now go make it happen!",
    "You were meant for great things!"
]

# Displaying the title
print("----- Welcome to the Magic 8 Ball! -----")
print()

# Taking a question from the user
question = input("Ask me any yes or no question: ")

# Displaying the response
print("\nThinking...\n")
print(random.choice(responses))
