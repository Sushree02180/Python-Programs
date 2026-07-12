# Program: Pet Personality Test

# Taking input from the user
pet = input("What's your favourite pet? ")

# Converting the input to lowercase
pet = pet.lower()

print("\n----- Pet Personality Test -----")

# Checking the user's favourite pet
if pet == "dog":
    print("🐶 You're loyal, friendly, and always ready for an adventure!")

elif pet == "cat":
    print("🐱 You're independent, curious, and enjoy your own space.")

elif pet == "rabbit":
    print("🐰 You're gentle, kind, and full of positive energy.")

elif pet == "parrot":
    print("🦜 You're talkative, confident, and love being around people.")

elif pet == "fish":
    print("🐠 You're calm, patient, and prefer a peaceful environment.")

elif pet == "turtle":
    print("🐢 You're wise, patient, and believe slow and steady wins the race.")

else:
    print("✨ Every pet is unique, just like you!")
