# Lab 03

## Exercise 1

1. **Question Discription:**

    Write an interactive Python3 program that prompts for and reads an integer number between 1,100 and 999,999. It then prints the number with a comma separating the thousand.
    **Hint**: use % and // division.  Also assume that the number formed by the last 3 digits is >= 100.

2. **Sample Runs** (user input is in bold):

    Please enter a number between 1,100 and 999,999: **1234**<br>
    1,234

    ---
    Please enter a number between 1,100 and 999,999:  **45786**<br>
    45,786

    ---
    Please enter a number between 1,100 and 999,999: **999999**<br>
    999,999

**My Solution**: [exercise1.py](exercise1.py)

## Exercise 2

1. **Question Discription:**

    Write an interactive Paython3 program that prompts and reads a student’s first name and year of birth. It then creates and prints the student password. The student password is formed as follows:

   - Student’s first name in lowercase.
   - Followed by last character in uppercase
   - Followed by first character in uppercase
   - Followed by $ character
   - Followed by student’s year of birth * 2

2. **Sample Runs** (user input is in bold):

    Enter student's first name: **MUHSIN**<br>
    Enter student's year of birth: **1982**<br>
    Password = muhsinNM$3964

    ---
    Enter student's first name: **Saleem**<br>
    Enter student's year of birth: **2005**<br>
    Password = saleemMS$4010

**My Solution**: [exercise2.py](exercise2.py)

## Exercise 3

1. **Question Discription:**

    Write an interactive Python3 program that prompts for a measurement in kilometers. It then converts it to miles, feet, and inches.

    **Note:**

    $$1\ mi = 1.609344\ km$$

    $$1\ mi = 5280\ ft$$

    $$1\ ft = 12\ in$$

2. **Sample Runs** (user input is in bold):

    Enter distance in kilometers: **626.5**<br>
    626.50 kilometers equals 389 miles, 1526 feet and 2.33 inches

    ---
    Enter distance in kilometers: **8.0**<br>
    8.00 kilometers equals 4 miles, 5126 feet and 8.63 inches

    ---
    Enter distance in kilometers: **1.2**<br>
    1.20 kilometers equals 0 miles, 3937 feet and 0.09 inches

**My Solution**: [exercise3.py](exercise3.py)
