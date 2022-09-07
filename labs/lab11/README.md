# Lab 11

## Exercise 1

1. **Question Description**:

    Define a `class Point` that represents a point in $2-D$ plane. The point has $x$ and $y$ coordinates. Define the following:

    - A constructor to initialize the $x$, $y$ coordinates.
    - A method `translate(self, dx,dy)` to translate the point object `dx`, and `dy` units in $x$ and $y$ directions, respectively.
    - A method `distanceTo (self, point)`  to return the distance between the point referenced by `self` and `point`.
    - `getX(self)` to return the value of $x$ coordinate.
    - `getY(self)` to return the value of $y$ coordinate.

2. **Sample Runs** (user input is in bold):

    - Creating 2 point objects; one with (3,5) as x,y coordinates; the second with (-10,30) as x,y coordinates.
    - Move the first point 5.5 units in x direction and -12.5 units in y direction using translate method.
    - Find the distance between the 2 points in their current location using distanceTo method.

    Coordinates of point 1 = (3.0, 5.0)<br>
    Coordinates of point 2 = (-10.0, 30.0)<br>
    After move<br>
    Coordinates of point 1 = (8.5, -7.5)<br>
    Distance between the 2 points = 41.82

**My Solution**: [exercise1.py](exercise1.py)

## Exercise 2

1. **Question Description**:

    Implement a `class Car` with the following properties. A car has a certain fuel efficiency (measured in km/liter) and a certain amount of fuel in the tank. The efficiency is specified in the constructor, and the initial fuel 0. Supply a method `drive` that simulates driving the car for a certain distance, reducing the fuel in the tank, a method `getFuel` to return the amount of fuel in the tank, and a method `addFuel` to fill the tank with an amount.

2. **Sample Runs** (user input is in bold):

    Sample code:

    ```python
    myCar = Car(50) # 50 km per liter

    myCar.addFuel(20) # fill tank with 20 liters

    myCar.drive(100) # Drive 100 km

    print("The remaining fuel is", myCar.getFuel()) # Print fuel remaining
    ```

    The remaining fuel is 18.0

**My Solution**: [exercise2.py](exercise2.py)
