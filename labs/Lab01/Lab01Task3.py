##
# This program calculate the area and circumference.
#

# Write your code below this line

#%% My code from what I learned in class

# Defining the constant PI
PI = 3.14159

# Setting the value of the radius
radius = 10

# Calculate the area in unit square
area = PI * radius * radius

# Calculate the circumference in unit
circumference = 2 * PI * radius

# Print the result
print("The area is", area, "units square and circumference is", circumference, "units, of the 10 units radius.")

#####################################################################################################################
#%% My code from what I learned outside of class

# import pi as PI from math module
from math import pi as PI

# Ask the user to enter the radius
user_radius = input("Enter the radius of the circle: ")

# Check if user has enter a float numbet
try:
    # If he did so, convert it to float
    float_radius=float(user_radius)
except ValueError:
    # If he did not, print an error message and exit the program
    print("You have entered an invalid value.")
    exit()

# Calculate the area in unit square
area = PI * float_radius ** 2

# Calculate the circumference in unit
circumference = 2 * PI * float_radius

# Print the result
print("The area is %.2f units square and circumference is %.2f units, of the 10 units radius." %(area, circumference))