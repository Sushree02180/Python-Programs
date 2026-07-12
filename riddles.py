# Program: Riddles

# Creating a dictionary of riddles and their answers
quiz = {
    "What comes once in a minute, twice in a moment, but never in a thousand years? ": "M",
    "I have keys but no locks. I have space but no room. You can enter but can't go outside. What am I? ": "Keyboard",
    "What has hands but cannot clap? ": "Clock",
    "What gets wetter the more it dries? ": "Towel",
    "What has to be broken before you can use it? ": "Egg",
    "What has one eye but cannot see? ": "Needle",
    "What can travel around the world while staying in one corner? ": "Stamp",
    "The more you take, the more you leave behind. What am I? ": "Footsteps",
    "What has a neck but no head? ": "Bottle",
    "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? ": "Echo"
}

# Initializing the score
score = 0

print("----- Welcome to the Riddles Game! -----")
print("Answer the following riddles.\n")

# Asking the riddles one by one
for question in quiz:
    answer = input(question)

    # Checking if the answer is correct
    if answer.lower() == quiz[question].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!")
        print("The correct answer is:", quiz[question], "\n")

# Displaying the final score
print("----- Riddles Completed -----")
print("Your Score:", score, "out of", len(quiz))

# Displaying a message based on the score
if score == len(quiz):
    print("Outstanding! You solved every riddle! 🎉")
elif score >= 7:
    print("Great job! You're a riddle master. 😎")
elif score >= 4:
    print("Nice effort! Keep practicing. 😊")
else:
    print("Better luck next time! Try again. 💪")
