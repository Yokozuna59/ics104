# Function for choice a
def moveEvenNumbers(userList):
    movedList = []
    for element in userList:
        # If element if even move it to beginning of the list
        if (element%2 == 0):
            movedList.insert(0, element)
        # else move it to the end of the list
        else:
            movedList.append(element)
    return movedList

# Function for choice b
def getSecondMaxNumber(userList):
    userListCopy = userList.copy()
    maxNumber = max(userListCopy)
    numberOfMaxNumbers = userListCopy.count(maxNumber)

    # Remove all max number occurrence
    for _ in range(numberOfMaxNumbers):
        userListCopy.remove(maxNumber)
    secondMaxNumber = max(userListCopy)
    return secondMaxNumber

# Function for choice c
def replaceByLargeNeighbors(userList):
    userListCopy = userList.copy()
    for index in range(len(userListCopy)):
        # continure of the element is the first or last in the list
        if (index != 0) and (index != (len(userListCopy) - 1)):
            # Get the max number between the element before and after the current element
            maxNumber = max(userListCopy[index - 1], userListCopy[index + 1])
            userListCopy[index] = maxNumber
    return userListCopy

def main():
    userList = [1, 6, 3, 4, 5, 2, 8, 5]


    # Get user input
    userChoice = input("Enter choice: ").lower()

    # Check if user input is a
    if userChoice == "a":
        movedList = moveEvenNumbers(userList)
        print("The list after operation:", movedList)
    # Check if user input is b
    elif userChoice == "b":
        secondMaxNumber = getSecondMaxNumber(userList)
        print("The second largest:", secondMaxNumber)
    # Check if user input is c
    elif userChoice == "c":
        replacedList = replaceByLargeNeighbors(userList)
        print("The list after operation:", replacedList)
    # Check if user input is not a nor b nor c
    else:
        # Print wrong choice
        print("Wrong choice")

main()