##
# This program reads the user time in HH:MM form and checks if it is valid or not.
#

# Ask the user to enter time in HH:MM form
userTime = input("Enter the time in the form of HH:MM: ")

# Check if the user has enter the correct length of time format
if (len(userTime) == 5):
    # Check if the user has entered a colom as the third character
    if (userTime[2] == ":"):
        # Get the hours and minutes characters
        hours = userTime[0:2]
        minutes = userTime[3:5]

        # Check if hours and minutes are digits
        if (hours.isdigit() and minutes.isdigit()):
            # Convert hours and minutes into integers
            hours = int(hours)
            minutes = int(minutes)

            # Check if hours are in range
            if (0 <= hours <= 23):
                # Check if minutes are in range
                if (0 <= minutes <= 59):
                    errorType = None
                else:
                    errorType = "Invalid number of (minutes out of range)"
            else:
                errorType = "Invalid number of hours (out of range)"
        else:
            errorType = "Invalid character in input"
    else:
        errorType = "Invalid input format"
else:
    errorType = "Invalid input length"

# Print the result
if (errorType == None):
    # Print `Valid`` if it is a valid time
    print("Valid time.")
else:
    # Print `Invalid Time` if it is an invalid time
    print("Invalid time.")

    # Print the error type
    print("Error Type: %s" %errorType)