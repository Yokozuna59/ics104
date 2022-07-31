def isFloat(string):
    try:
        return float(string)
    except ValueError:
        return False


def main():
    userInput = input("Enter an input: ")
    if isFloat(userInput):
        print("The input is float")
    else:
        print("The input is not float")

main()
