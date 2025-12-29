from abc import ABC, abstractmethod

# Implementor Interface
class Implementor(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass

# Concrete Implementor Classes
class AddCalculation(Implementor):
    def calculate(self, a: float, b: float) -> float:
        return a + b

class MultiplyCalculation(Implementor):
    def calculate(self, a: float, b: float) -> float:
        return a * b

# Abstraction Interface
class Abstraction(ABC):
    def __init__(self, calculation: Implementor, numbers: list[float]):
        self.calculation = calculation
        self.numbers = numbers
    
    @abstractmethod
    def print(self, n: float) -> None:
        pass

# Refined Abstraction Classes
class Numbers(Abstraction):
    def print(self, n: float) -> None:
        for number in self.numbers:
            print(self.calculation.calculate(number, n))

add = AddCalculation()
multiply = MultiplyCalculation()

numbers = Numbers(add, [1, 2, 3, 4])
numbers.print(2)

print("==========")

numbers2 = Numbers(multiply, [1, 2, 3, 4])
numbers2.print(2)

