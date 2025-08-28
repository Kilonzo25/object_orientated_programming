class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} is moving"

# Different vehicles with same method, different behavior
class Car(Vehicle):
    def move(self):
        return (f" {self.name} is driving")

class Plane(Vehicle):
    def move(self):
        return (f"{self.name} is flying")

class Boat(Vehicle):
    def move(self):
        return (f" {self.name} is sailing")

class Bike(Vehicle):
    def move(self):
        return (f" {self.name} is pedaling")

# Test polymorphism - same method, different results!
vehicles = [
    Car("Honda"),
    Plane("Boeing"),
    Boat("Titanic"),
    Bike("Mountain Bike")
]

print(" POLYMORPHISM IN ACTION!")
for vehicle in vehicles:
    print(vehicle.move())  # Same method call, different behaviors!