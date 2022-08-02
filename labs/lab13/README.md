# Lab 13

## Exercise 1

1. **Question Discription:**

    Write a program that reads in three integers and prints "in order" if they are sorted in ascending or descending order, or "not in order" otherwise.

2. **Sample Runs** (user input is in bold):

    Enter first number: **1**<br>
    Enter second number: **2**<br>
    Enter third number:**5**<br>
    1 2 5 in order

    ---
    Enter first number: **1**<br>
    Enter second number: **5**<br>
    Enter third number: **2**<br>
    1 2 5 not in order

    ---
    Enter first number: **5**<br>
    Enter second number: **2**<br>
    Enter third number: **1**<br>
    1 2 5 in order

    ---
    Enter first number: **1**<br>
    Enter second number: **2**<br>
    Enter third number: **2**<br>
    1 2 2 in order

**My Solution**: [exercise1.c](exercise1.c)

## Exercise 2

1. **Question Description**:

    Write a program that reads an integer value and prints all of its binary digits in reverse order: Print the remainder (number % 2), then replace the number with number // 2. Keep going until the number is 0.

2. **Sample Runs** (user input is in bold):

    Enter an integer: **13**<br>
    The binary digits in reverse order are 1011

    ---
    Enter an integer: **38**<br>
    The binary digits in reverse order are 011001

**My Solution**: [exercise2.c](exercise2.c)

## Exercise 3

1. **Description**:

    Write a loop that reads positive numbers from the user and sum them. The loop continues till a negative number is entered. Your program then prints the result. If the user enter a negative value from the beginning, your code should display: 'No positive number was entered'. You should include the empty string in your loop without any error (i.e. read the first sample run).

2. **Sample Runs** (user input is in bold):

    Enter a positive number (or a negative value to finish):**5**<br>
    Enter a positive number (or a negative value to finish):**2**<br>
    Enter a positive number (or a negative value to finish):**4**<br>
    Enter a positive number (or a negative value to finish):**-5**<br>
    Sum = 11.0

    ---
    Enter a positive number (or a negative value to finish):**-8**<br>
    No positive number was entered.

**My Solution**: [exercise3.c](exercise3.c)

## Exercise 4

1. **Description**:

    Write a function `isPrime` that has one integer parameter n. The function returns 1 if n is prime or 0 otherwise.<br>
    Use the function to print all the prime numbers less than 100.

2. **Sample Runs** (user input is in bold):

    2<br>
    3<br>
    5<br>
    7<br>
    11<br>
    13<br>
    17<br>
    19<br>
    23<br>
    29<br>
    31<br>
    37<br>
    41<br>
    43<br>
    47<br>
    53<br>
    59<br>
    61<br>
    67<br>
    71<br>
    73<br>
    79<br>
    83<br>
    89<br>
    97

**My Solution**: [exercise4.c](exercise4.c)
