# Program: Countdown Timer

# Taking the starting number from the user
count = int(input("Enter the starting number: "))

# Displaying the countdown
print("\nCountdown begins!\n")

while count > 0:
    print(count)
    count -= 1

print("Time's up!")
