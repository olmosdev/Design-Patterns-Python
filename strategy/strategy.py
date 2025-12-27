from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b
    
class MulStrategy(Strategy):
    def execute(self, a, b):
        return a * b

# Creating the context        
# This class will contain an IStrategy type so it can receive any class that inherits from it
class Operation:
    def __init__(self, strategy: Strategy):
        self.__strategy = strategy

    def calculate(self, a, b):
        return self.__strategy.execute(a, b)
    
    def set_strategy(self, strategy: Strategy):
        self.__strategy = strategy

# Seing how to work
add_strategy = AddStrategy()
mul_strategy = MulStrategy()

operation = Operation(add_strategy)
print(operation.calculate(5, 7))
operation.set_strategy(mul_strategy)
print(operation.calculate(5, 7))

