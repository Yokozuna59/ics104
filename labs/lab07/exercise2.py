##
# This program prints the number of vowels in a string.
#

# Ask user to enter a word
userWord = input("Enter a word: ")

# Initialize the counter
count = 0

# While loop until the end of the word
for letter in userWord:
    # Check if the character is a vowel
    if (letter in "aeiou"):
        # Add 1 to the counter
        count += 1

# Print the result
print("There are %d vowels in science", count)