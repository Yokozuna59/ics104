##
# This programs reads user input asking for wavelength and frequency,
# Then ask user to enter the wavelength or frequency value,
# Then prints the electromagnetic type.
#

# Ask user to enter either W for wavelength or F for frequency
userInput = input("Please enter a letter (W) for a wavelength or (F) for frequency: ")

# Check if user input is W or F
if (userInput == "W"):
    userChoice = "wavelength"
elif (userInput == "F"):
    userChoice = "frequency"

# Ask usr to enter the value of the wavelength or frequency
userValueFloat = float(input("Please enter the %s: " %userChoice))

if (userInput == "W"):
    # Check wavelength range value
    if (1e-1 <= userValueFloat):
        electromagneticType = "Radio Wave"
    elif (1e-3 <= userValueFloat < 1e-1):
        electromagneticType = "Microwaves"
    elif (7e-7 <= userValueFloat < 1e-3):
        electromagneticType = "Infrared"
    elif (4e-7 <= userValueFloat < 7e-7):
        electromagneticType = "Visible Light"
    elif (1e-8 <= userValueFloat < 4e-7):
        electromagneticType = "Ultraviolet"
    elif (1e-11 <= userValueFloat < 1e-8):
        electromagneticType = "X-Rays"
    elif (0 <= userValueFloat < 1e-11):
        electromagneticType = "Gamma Rays"
elif (userInput=="F"):
    # Check frequency range value
    if (0 <= userValueFloat < 3e9):
        electromagneticType = "Radio Wave"
    elif (3e9 <= userValueFloat < 3e11):
        electromagneticType = "Microwaves"
    elif (3e11 <= userValueFloat < 4e14):
        electromagneticType = "Infrared"
    elif (4e14 <= userValueFloat < 7.5e14):
        electromagneticType = "Visible Light"
    elif (7.5e14 <= userValueFloat < 3e16):
        electromagneticType = "Ultraviolet"
    elif (3e16 <= userValueFloat < 3e19):
        electromagneticType = "X-Rays"
    elif (userValueFloat >= 3e19):
        electromagneticType = "Gamma Rays"

# Print the electromagnetic type
print("Electromagnetic Spectrum type is: %s" %electromagneticType)