# Homework 1

## Question 1 (30 points)

1. **Grade Distribution:**

   - Correct Code: 25 points.
   - Programming Style (comments and variable names): 5 points.

2. **Question Description:**

    Develop a program that begins by reading a number of seconds from the user. Then your program should display the equivalent amount of time in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that they occupy exactly two digits, with a leading 0 displayed if necessary.

3. **Sample Runs** (user input is in bold):

    Please enter an integer number representing a number of seconds: **369121517**<br>
    Equivalent amount of time: 4272:05:45:17

**My Solution:** [quesion1.py](quesion1.py)

## Question 2 (30 points)

1. **Grade Distribution:**

   - Correct Code: 25 points.
   - Programming Style (comments and variable names): 5 points.

2. **Question Description:**

    Write a program that transforms numbers 1, 2, 3, …, 12 into the corresponding month names January, February, March, …, December. In your solution, make a long string "January February March ...", in which you add spaces such that each month name has the same length. Then concatenate the characters of the month that you want. Before printing the month use the strip method to remove trailing spaces.
    **Note:** Use the material Covered in Chapter 2. Don’t use if statements.

3. **Sample Runs** (user input is in bold):

    Please enter an integer number representing a month (between 1 and 12): **7**<br>
    Your month is July.

**My Solution:** [quesion2.py](quesion2.py)

## Question 3 (40 points)

1. **Grade Distribution:**

   - Correct Code: 35 points.
   - Programming style (comments and variable names): 5 points.

2. **Question Description:**

    Write a program that prompts the user for a wavelength (W) value or a frequency (F) value and prints a description of the corresponding part of the electromagnetic spectrum, as given in the following table.

    | Type | Wavelength (m) | Frequency (Hz) |
    |:----:|----------------|----------------|
    | Radio Wave | $[10^{-1},\ \infty)$ | $[0,\ 3 \times 10^{9})$ |
    | Microwaves | $[10^{-3},\ 10^{-1})$ | $[3 \times 10^{9},\ 3 \times 10^{11})$ |
    | Infrared | $[7 \times 10^{-7},\ 10^{-3})$ | $[3 \times 10^{11},\ 4 \times 10^{14})$ |
    | Visible Light | $[4 \times 10^{-7},\ 7 \times 10^{-7})$ | $[4 \times 10^{14},\ 7.5 \times 10^{14})$ |
    | Ultraviolet | $[10^{-8},\ 4 \times 10^{-7})$ | $[7.5 \times 10^{14}, 3 \times 10^{16})$ |
    | X-Rays | $[10^{-11}, 10^{-8})$ | $[3 \times 10^{16}, 3 \times 10^{19})$ |
    | Gamma Rays | $[0, 10^{-11})$ | $[3 \times 10^{19},\ \infty)$ |

    The user should input "W" for wavelength or "F" for frequency. The input units for frequency should be hertz (Hz) and the input units for wavelength should be meters (m).
    **Hint**: To understand the mathematical intervals [x, y], (z, w) please review mathematical numerical ranges. (inclusive or exclusive)

3. **Sample Runs** (user input is in bold):

    Please enter a letter (W) for a wavelength or (F) for frequency: **F**<br>
    Please enter the frequency: **6.5E14**<br>
    Electromagnetic Spectrum type is: Visible light

    ---

    Please enter a letter (W) for a wavelength or (F) for frequency: **W**<br>
    Please enter the wavelength: **5.0E-9**<br>
    Electromagnetic Spectrum type is: X-rays

**My Solution:** [quesion3.py](quesion3.py)
