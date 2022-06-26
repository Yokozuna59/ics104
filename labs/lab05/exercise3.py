##
# This program reads user input asking for a character, then prints if the character is a vowel or consonant or have wrong input.
#

# Ask user to enter one character
userLetter = input("Enter one character: ").lower()

# Check if the user entered a letter of the length of one
if (len(userLetter) == 1):
    # Check if the user entered a letter
    if (userLetter.isalpha()):
        # Check if the user entered a vowel
        if (userLetter in "aeiou"):
            output = "Vowel."
        else:
            output = "Consonant."
    else:
        output = "That was neither a vowel nor a consonant."
else:
    output = "That input didn't have a valid length."

# Print the result
print(output)