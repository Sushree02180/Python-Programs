# Program: Word Counter

# Function to count the number of words
def count_words(sentence):
    words = sentence.split()
    return len(words)

# Taking input from the user
sentence = input("Enter a sentence: ")

# Calling the function
word_count = count_words(sentence)

# Displaying the result
print("Number of words:", word_count)
