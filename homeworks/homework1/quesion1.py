##
# This prgram calculates the number of days, hours, minutes and seconds from an user input time in seconds.
#

# Constants
SECONDS_IN_A_MINUTE = 60 # Number of seconds in a minute

MINUTES_IN_A_HOUR = 60 # Number of minutes in an hour
SECONDS_IN_A_HOUR = SECONDS_IN_A_MINUTE * MINUTES_IN_A_HOUR # Number of seconds in an hour; 60 * 60 = 3600

HOURS_IN_A_DAY = 24 # Number of hours in a day
SECONDS_IN_A_DAY = SECONDS_IN_A_HOUR * HOURS_IN_A_DAY # Number of seconds in a day; 24 * 3600 = 86400

# Ask user to enter number of seconds
userSeconds = int(input("Please enter an integer number representing a number of seconds: "))

# Calculate number of seconds
numberOfSeconds = userSeconds % SECONDS_IN_A_MINUTE

# Calculate number of minutes
remainingMinutes = userSeconds % SECONDS_IN_A_HOUR
numberOfMinutes = remainingMinutes // SECONDS_IN_A_MINUTE

# Calculate the number of hours
remainingHours = userSeconds % SECONDS_IN_A_DAY
numberOfHours = remainingHours // SECONDS_IN_A_HOUR

# Calculate number of days
numberOfDays = userSeconds // SECONDS_IN_A_DAY

# Print the number of days, hours, minutes and seconds
print("Equivalent amount of time: %d:%02d:%02d:%02d" %(numberOfDays, numberOfHours, numberOfMinutes, numberOfSeconds))