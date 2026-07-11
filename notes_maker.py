# Program: Notes App

# Taking a note from the user
note = input("Enter your note: ")

# Writing the note to a file
file = open("notes.txt", "w")
file.write(note)
file.close()

# Reading the note from the file
file = open("notes.txt", "r")
saved_note = file.read()
file.close()

# Displaying the saved note
print("\n----- Saved Note -----")
print(saved_note)
