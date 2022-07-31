class Car:
    def __init__(self, efficiency):
        self._efficiency = efficiency
        self._fuel = 0

    def driver(self, distance):
        self._fuel -= distance/self._efficiency

    def getFuel(self):
        return self._fuel

    def addFuel(self, fuel):
        self._fuel += fuel

myCar = Car(50)
myCar.addFuel(20)
myCar.driver(100)
print("The remaining fuel is", myCar.getFuel())
