# Homework 3

## Question 1 (35 points)

1. **Grade Distribution:**

   - Correct Code: 30 points.
   - Programming Style (comments and variable names): 5 points.

2. **Question Description:**

    A charity organization needs a program to calculate the amount of financial assistance for needy families based on the following conditions:

    | Annual Income | Number of Children | Financial Assistance per Childe |
    |:-------------:|:------------------:|:---------------------:|
    | [\$0, \$20000) | $[1, \infty)$ | \$2000 |
    | [\$20000, \$30000) | $[2, \infty)$ | \$1500 |
    | [\$30000, \$40000] | $[3, \infty)$ | \$1000 |
    | Otherwise | $[0, \infty)$ | No Financial Assistance |

    Implement a function for this computation. Write a program that asks the user to input the household income and number of children for each applicant, printing the amount returned by your function. Use $–1$ as a sentinel value for the input. On exiting the program should print the total amount of assistance given to all families. Note the followings:

    1. Carefully read the question and observe the sample runs.
    2. Use function and loop.
    3. Follow best programming practice.

3. **Sample Runs** (user input is in bold):

    Enter the household income: **40000**<br>
    Enter the number of children: **4**<br>
    Amount of assistance: 4000<br>
    Enter the household income: **-1**<br>
    Exit<br>
    The total amount of assistance: 4000

    ---
    Enter the household income: **15000**<br>
    Enter the number of children: **3**<br>
    Amount of assistance: **6000**<br>
    Enter the household income: **25000**<br>
    Enter the number of children: **5**<br>
    Amount of assistance: **7500**<br>
    Enter the household income: **70000**<br>
    Enter the number of children: **1**<br>
    Amount of assistance: **0**<br>
    Enter the household income: **-1**<br>
    Exit<br>
    The total amount of assistance: 13500

    ---
    Enter the household income: **-1**<br>
    Exit<br>
    The total amount of assistance: 0

**My Solution:** [quesion1.py](quesion1.py)

## Question 2 (45 points)

1. **Grade Distribution:**

   - Correct Code: 40 points.
   - Programming Style (comments and variable names): 5 points.

2. **Question Description:**

    Write list functions that carry out the following 3 tasks for a list of integers:

    a. Move all even elements to the front, otherwise preserving the order of the elements.<br>
    b. Print the second-largest element in the list.<br>
    c. Replace each element except the first and last by the larger of its two neighbors.

    Then, your program should take a user input as choice and demonstrate the working of the each of the task upon entering the choice as; 'a' for task (a), 'b' for task (b) and 'c' for task (c).

    **Note**: Consider the input list = [1, 6, 3, 4, 5, 2, 8, 5].

3. **Sample Runs** (user input is in bold):

    Enter choice: **a**<br>
    The list after operation: [8, 2, 4, 6, 1, 3, 5, 5]

    ---
    Enter choice: **b**<br>
    The second largest: 6

    ---
    Enter choice: **c**<br>
    The list after operation: [1, 3, 4, 5, 5, 8, 8, 5]

    ---
    Enter choice: **g**<br>
    Wrong choice

**My Solution:** [quesion2.py](quesion2.py)

## Question 3 (20 points)

1. **Grade Distribution:**

   - Correct Code: 15 points.
   - Programming style (comments and variable names): 5 points.

2. **Question Description:**

    Given a dictionary:<br>
    gradeCounts = { "A": 8, "D": 3, "B": 15, "F": 2, "C": 6 }

    Write the Python statements to print:

    1. all the keys.
    2. all the values.
    3. all the key and value pairs.
    4. all of the key and value pairs in key order.
    5. the average value.

3. **Sample Runs** (user input is in bold):

    The keys are:<br>
    A D B F C<br>
    The values are:<br>
    8 3 15 2 6<br>
    The key:value pairs:<br>
    A 8<br>
    D 3<br>
    B 15<br>
    F 2<br>
    C 6<br>
    The key:value pairs in key order:<br>
    A 8<br>
    B 15<br>
    C 6<br>
    D 3<br>
    F 2<br>
    Average of the values:<br>
    6.8

**My Solution:** [quesion3.py](quesion3.py)
