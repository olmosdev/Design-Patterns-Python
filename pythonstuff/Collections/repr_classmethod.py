class Car:
    def __init__(self, speed: int = 0):
        self.speed = speed
        
    def accelerate(self, acceleration: int = 10) -> None:
        self.speed += acceleration
        
    def start(self) -> None:
        print("Car started")
        
class CarWithRepr(Car):
    def __repr__(self) -> str:
        return f"Car with speed: {self.speed} km/h"
        
ferrari = Car()
print(ferrari)

bugati = CarWithRepr()
print(bugati)