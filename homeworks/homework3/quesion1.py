def main():
    finished = False
    totalAssistance = 0

    while not finished:
        # Get user input for household
        userIncome = int(input("Enter the household income: "))
        # chekc if user did not entered -1
        if (userIncome != -1):
            userChileds = int(input("Enter the number of children: "))

            # check the range of user income and child numbers
            if (0 <= userIncome < 20000):
                currentAssistance = 2000 * userChileds
            elif (20000 <= userIncome < 30000) and (userChileds >= 2):
                currentAssistance = 1500 * userChileds
            elif (30000 <= userIncome <= 40000) and (userChileds >= 3):
                currentAssistance = 1000 * userChileds
            else:
                currentAssistance = 0

            # Print currentAssistance and add it to totalAssistance
            print("Amount of assistance:", currentAssistance)
            totalAssistance += currentAssistance
        # Else exit loop
        else:
            print("Exit")
            finished = True
    print("The total amount of assistance:", totalAssistance)

main()