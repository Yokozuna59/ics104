# Homework 2

## Question 1 (30 points)

1. **Grade Distribution:**

   - Correct Code: 25 points.
   - Programming Style (comments and variable names): 5 points.

2. **Question Description:**

    Write a Python program that implements the Taylor series expansion of the function $ln(1 + x)$ for any $x$ in the interval $(-1,1]$, as given by:

    $$ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} - ...$$

    The program prompts the user to enter the number of terms $n$. If $n > 0$, the program prompts the user to enter the value of $x$. If the value of $x$ is in the interval $(-1, 1]$, the program calculates the approximation to $ln(1+x)$ using the first $n$ terms of the above series. The program prints the approximate value.

    **Note**: the program should validate the user input for different values. If an invalid value is entered, the program should output an appropriate error messages and loops as long as the input is not valid.

3. **Sample Runs** (user input is in bold):

    Enter number of terms: **0**<br>
    Error: Zero or negative number of terms not accepted<br>
    Enter the number of terms: **9000**<br>
    Enter the value of x in the interval (-1, 1]: **-2**<br>
    Error: Invalid value for x<br>
    Enter the value of x in the interval (-1, 1]: **0.5**<br>
    The approximate value of ln(1+0.5000) up to 9000 terms is 0.4054651081

**My Solution:** [quesion1.py](quesion1.py)

## Question 2 (30 points)

1. **Grade Distribution:**

   - Correct Code: 25 points.
   - Programming Style (comments and variable names): 5 points.

2. **Question Description:**

    Write a Python program that reads a word and prints all substrings, sorted by length, or an empty string to terminate the program. Printing all substring must be done by a function call it printSubstrings which takes a string as its parameter.  The program must loop to read another word until the user enter an empty string.

3. **Sample Runs** (user input is in bold):

    Enter a string or an empty string to terminate the program: **sit**<br>
    s<br>
    i<br>
    t<br>
    si<br>
    it<br>
    sit<br>
    Enter a string or an empty string to terminate the program: **Code**<br>
    C<br>
    o<br>
    d<br>
    e<br>
    Co<br>
    od<br>
    de<br>
    Cod<br>
    ode<br>
    Code<br>
    Enter a string or an empty string to terminate the program:<br>
    Done…

**My Solution:** [quesion2.py](quesion2.py)

## Question 3 (40 points)

1. **Grade Distribution:**

   - Correct Code: 35 points.
   - Programming style (comments and variable names): 5 points.

2. **Question Description:**

    Write a Python program that asks the user for an integer $n$ and then prints out all its prime factors. In your program, you have to create a function called isPrime that takes an integer as its parameter and returns a Boolean value (True/False).

    **Hint**: $i$ is not a prime, if $i$ has a divisor that is greater than $1$ and less than or equal to sqrt($i$).

3. **Sample Runs** (user input is in bold):

    Enter an integer: **156**<br>
    Prime factors:<br>
    2<br>
    2<br>
    3<br>
    13

    ---
    Enter an integer: **150**<br>
    Prime factors:<br>
    2<br>
    3<br>
    5<br>
    5

    ---
    Enter an integer: **11**<br>
    Prime factors:<br>
    11

**My Solution:** [quesion3.py](quesion3.py)
