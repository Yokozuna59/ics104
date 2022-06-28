##
# This program print a sequence of table using nested for loops.
#

# Exercise 1
for i in range(1, 6):
    print("%s " %i * 5)

# Print Empty Line
print()

# Exercise 2
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

# Print Empty Line
print()

# Exercise 3
for i in range(1, 6):
    for j in range(1, i+1):
        print("%s" %j, end=" ")
    print()

# Print Empty Line
print()

# Exercise 4
for i in range(1, 6):
    for j in range(i, 6):
        print("%s" %j, end=" ")
    print()

# Print Empty Line
print()

# Exercise 5
for i in range(5, 0, -1):
    print("*" * i)

# Print Empty Line
print()

# Exercise 6
for i in range(5, 0, -1):
    print(6-i, "*" * i)