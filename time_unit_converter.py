# Time Unit Converter

# Function to convert minutes to seconds
def minutes_to_seconds(minutes):
    return minutes * 60

# Taking input from the user
minutes = int(input("Enter time in minutes: "))

# Calling the function
seconds = minutes_to_seconds(minutes)

# Displaying the result
print("Time in seconds:", seconds)
