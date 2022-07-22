##
# This program that adds all numbers from 2 to 10,000 to a list.
# Remove the multiples of 2 (but not 2), multiples of 3 (but not 3), and so on, up to the multiples of 100.
# Print the remaining values.
#

# Create a list with elements from 2 to 10000
numbers = []
for number in range(2, 10001):
    numbers.append(number)

# Remove the multiples from 2 to 100, but not from 2 to 100
for multiples in range(2, 101):
    for number in numbers:
        if (number % multiples == 0) and (number != multiples):
            numbers.remove(number)

# Print result
print(numbers)