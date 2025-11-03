# polymorphism_challenge.py

class Vehicle:
    def move(self):
        pass  # base method, overridden by child classes


class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")


class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling 🚴")


# Demonstration of polymorphism
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
