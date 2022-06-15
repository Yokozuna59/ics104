##
# This program converts temperature from Celsius into Fahrenheit.
#

# Write your code below this line

#%% My code from what I learned in class

# Setting the Celsius value first
celsius = 100

# Calculate the temperature from Celsius into Fahrenheit
fahrenheit = (9 * celsius)/5 + 32

# Print the result
print("The", celsius, "Celsius is", fahrenheit, "in Fahrenheit.")

#################################################################################
#%% My code from what I learned outside of class

# Ask the user to enter the temperature in Celsius
user_celsius = input("Enter the temperature in Celsius: ")

# Check if user has enter a float numbet
try:
    # If he did so, convert it to float
    float_celsius=float(user_celsius)
except ValueError:
    # If he did not, print an error message and exit the program
    print("You have entered an invalid value.")
    exit()

# Calculate the temperature from Celsius into Fahrenheit
convert_to_fahrenheit = (float_celsius * 9)/5 + 32

# Print the result
print("The %.2f Celsius is %.2f Fahrenheit." %(float_celsius, convert_to_fahrenheit))