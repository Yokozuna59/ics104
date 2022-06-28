# Lab 05

## Exercise 1

1. **Question Description**:

    A supermarket awards coupons depending on how much a customer spends on groceries. For example, if you spend $50, you will get a coupon worth eight percent of that amount. The following table shows the percent used to calculate the coupon awarded for different amounts spent:

    | Money Spent | Coupon Percentage |
    |:-----------:|:-----------------:|
    | $[0, 10)$ | %0 |
    | $[10, 60)$ | %8 |
    | $[60, 150)$ | %10 |
    | $[150, 210)$ | %12 |
    | $[210, \infty)$ | %14 |

    Write a program that calculates and prints the value of the coupon a person can receive based on groceries purchased.

2. **Sample Runs** (user input is in bold):

    Please enter the cost of your groceries: **7**<br>
    You win a discount coupon of $0.00. (0% of your purchase)

    ---
    Please enter the cost of your groceries: **59.9**<br>
    You win a discount coupon of $4.79. (8% of your purchase)

    ---
    Please enter the cost of your groceries: **210**<br>
    You win a discount coupon of $29.40. (14% of your purchase)

    ---
    Please enter the cost of your groceries: **-20.5**<br>
    The cost must be a positive value

**My Solution**: [exercise1.py](exercise1.py)

## Exercise 2

1. **Description**:

    Write a program that asks the user to enter a month (1 for January, 2 for February, and so on) and then prints the number of days in the month. For February, print “28 or 29 days”.
    **Note:** Do not use a separate if/else branch for each month. Use Boolean operators.
    **Hint:** Use given table to get the number of days in a month.

    | Month | Days |
    |:-----:|:----:|
    | 1 | 31 days |
    | 2 | 28 or 29 days |
    | 3 | 31 days |
    | 4 | 30 days |
    | 5 | 31 days |
    | 6 | 30 days |
    | 7 | 31 days |
    | 8 | 31 days |
    | 9 | 30 days |
    | 10 | 31 days |
    | 11 | 30 days |
    | 12 | 31 days |

2. **Sample Runs** (user input is in bold):

    Enter a month: **5**<br>
    30 days

    ---
    Enter a month: **6**<br>
    30 days

    ---
    Enter a month: **3**<br>
    31 days

    ---
    Enter a month: **2**<br>
    28 or 29 days

    ---
    Enter a month: **0**<br>
    Wrong input

**My Solution**: [exercise2.py](exercise2.py)

## Exercise 3

1. **Description**:

    Write a program that prompts the user to provide a single character from the alphabet.
    Print Vowel or Consonant, depending on the user input. If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message.

2. **Sample Runs** (user input is in bold):

    Enter one character: **python**
    That input didn't have a valid length.

    ---
    Enter one character: **B**<br>
    Vowel.

    ---
    Enter one character: **e**<br>
    28 or 29 days.

    ---
    Enter one character: **&**<br>
    That was neither a vowel nor a consonant.

**My Solution**: [exercise3.py](exercise3.py)
