from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Beer(Prototype):
    def __init__(self, name: str, brand: str, sizes: list[int]) -> None:
        self.name = name
        self.brand = brand
        self.sizes = sizes

    def clone(self):
        # return copy.copy(self)
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Name: {self.name}, Brand: {self.brand}, Sizes in milliliters: {self.sizes}"

"""
The main difference is that copy.copy() (shallow copy) creates a new object but 
references the internal elements of the original, while copy.deepcopy() creates 
a new object and recursively copies all the internal elements, guaranteeing 
complete independence
"""


beer = Beer("Pikantus", "Erdinger", [1000, 500])
print(beer)

beer_clone = beer.clone()
beer_clone.name = "Pikantus2"
beer_clone.sizes.append(250)
print(beer_clone)

print(beer)