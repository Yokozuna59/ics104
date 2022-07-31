# Lab 12

## Exercise 1

1. **Question Discription:**

   - Convert the following pseudo code into python. Run your program for different input values.
     - widthWithoutBlackTile = Total Width - Tile Width
     - Number of white-black tile pairs = the integer part of

        $$\frac{widthWithoutBlackTile}{(2 * TileWidth)}$$

     - Number of Tiles = 1 + 2 * Number of white-black tile pairs
     - Length of used tiles = Number of Tiles * Tile width
     - Total gap = Total Width - Length of used tiles
     - Gap at each end = Total gap / 2

2. **Sample Runs** (user input is in bold):

    Total Width = 23<br>
    Tile width = 2<br>
    Number of tiles 11<br>
    Gap on each sides = 0.5<br>
    Number of black tiles 6<br>
    Number of white tiles 5

**My Solution**: [exercise1.c](exercise1.c)

## Exercise 2

1. **Question Discription:**

    Write an interactive C program that prompts for and reads an integer number between 1,100 and 999,999. It then prints the number with a comma separating the thousand. Assume that the number formed by the last 3 digits is >= 100.<br>
    **Hint**: use % and / division.

2. **Sample Runs** (user input is in bold):

    Please enter a number between 1,100 and 999,999:  **2000**<br>
    2,000

    ---
    Please enter a number between 1,100 and 999,999: **45786**<br>
    45,786

    ---
    Please enter a number between 1,100 and 999,999: **999999**<br>
    999,999

**My Solutions**: [exercise2.c](exercise2.c)

## Exercise 3

1. **Question Discription:**

    Write an interactive C program that prompts for a measurement in kilometers. It then converts it to miles, feet, and inches.

    **Note:**

    $$1\ mi = 1.609344\ km$$

    $$1\ mi = 5280\ feet$$

    $$1\ ft = 12\ in$$

2. **Sample Runs** (user input is in bold):

    Enter distance in kilometers: **626.5**
    626.50 kilometers equals 389 miles, 1526 feet and 2.33 inches

    ---
    Enter distance in kilometers: **8.0**
    8.00 kilometers equals 4 miles, 5126 feet and 8.63 inches

    ---
    Enter distance in kilometers: **1.2**
    1.20 kilometers equals 0 miles, 3937 feet and 0.09 inches

**My Solutions**: [exercise3.c](exercise3.c)
