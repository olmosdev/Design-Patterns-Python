from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Beer(Prototype):
    def __init__(self, name: str, brand: str) -> None:
        self.name = name
        self.brand = brand

    def clone(self):
        return copy.copy(self)

    def __str__(self) -> str:
        return f"Name: {self.name}, Brand: {self.brand}"

beer = Beer("Lager", "Heineken")
print(beer)
beer_clone = beer.clone()
beer_clone.name = "Pikantus"
beer_clone.brand = "Erdinger"
print(beer_clone)