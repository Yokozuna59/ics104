##
# This program converts the user's input from kilometers to miles, feets, and inches.
#

# Write your code below this line

# Create constants for the conversion factors
MILE_TO_KILOMETERS = 1.609344
KILOMETER_TO_MILES = 1/MILE_TO_KILOMETERS # 0.621371192237334
MILE_TO_FEETS = 5280
FEET_TO_INCHES = 12

# Ask the user to enter the number of kilometers
userKilometers = float(input("Enter the number of kilometers: "))

# Convert the kilometers to miles
convertToMiles = userKilometers * KILOMETER_TO_MILES

# Convert remaining miles to feets
convertToFeets = convertToMiles % 1 * MILE_TO_FEETS

# Convert remaining feets to inches
convertToInches = convertToFeets % 1 * FEET_TO_INCHES

print("%.2f kilometers equals %d miles, %d feets and %.2f inches." %(userKilometers, convertToMiles, convertToFeets, convertToInches))