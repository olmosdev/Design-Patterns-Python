from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def get_quantity():
        pass

    def description(self):
        print("I am a drink")

class Beer(Drink):
    def __init__(self, quantity: int) -> None:
        self.__quantity = quantity

    def get_quantity(self) -> int:
        return self.__quantity

beer = Beer(15)
print(beer.get_quantity())
beer.description()