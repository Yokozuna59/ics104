##
# This program check if two user inputs are identical.
#

# Create function check if two tuple are identical
def isIdentical(a, b):
    if (len(a) == len(b)):
        for letter in a:
            if (a.count(letter) != b.count(letter)):
                return False
    else:
        return False
    return True

# Create main fuction were the code starts
def main():
    # Ask user for tuples
    a = tuple(input("Enter tuple a: ").split(" "))
    b = tuple(input("Enter tuple b: ").split(" "))

    if isIdentical(a, b):
        result = "The tuples are identical"
    else:
        result = "The tuples are not identical"

    # Print result
    print(result)

# Execute the main function
if __name__ == "__main__":
    main()