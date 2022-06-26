##
# This program reads user input asking for cost of groceries, then prints the discount and percentage.
#

# Ask the user to enter the cost of their groceries
userCost = float(input("Please enter the cost of your groceries: "))

# Check userCost range
if (userCost < 0):
    discountPercentage = -1
elif (0 <= userCost < 10):
    discountPercentage = 0
elif (10 <= userCost < 60):
    discountPercentage = 8
elif (60 <= userCost < 150):
    discountPercentage = 10
elif (150 <= userCost < 210):
    discountPercentage = 12
elif (userCost >= 210):
    discountPercentage = 14

# Print the result
if (discountPercentage != -1):
    discount = userCost * (discountPercentage / 100)
    print("You win a discount coupon of $%.2f. (%d%% of your purchase)" % (discount, discountPercentage))
else:
    print("The cost must be a positive value")