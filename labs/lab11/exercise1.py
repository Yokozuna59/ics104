from math import sqrt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def translate(self, dx, dy):
        self._x += dx
        self._y += dy

    def distanceTo(self, point):
        dx = self._x - point._x
        dy = self._y - point._y
        distance = sqrt(dx ** 2 + dy ** 2)
        return distance

    def getX(self):
        return self._x

    def getY(self):
        return self._y

def main():
    firstPoint = Point(3.0, 5.0)
    print("Coordinates of point 1 = (%.1f, %.1f)" %(firstPoint.getX(), firstPoint.getY()))

    secondPoint = Point(-10, 30)
    print("Coordinates of point 2 = (%.1f, %.1f)" %(secondPoint.getX(), secondPoint.getY()))

    print("After move")

    firstPoint.translate(5.5, -12.5)
    print("Coordinates of point 1 = (%.1f, %.1f)" %(firstPoint.getX(), firstPoint.getY()))

    print("Distance between the 2 points = %.2f" %firstPoint.distanceTo(secondPoint))

main()