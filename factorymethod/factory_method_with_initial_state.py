from abc import ABC, abstractmethod

class Concept(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def price(self) -> float:
        pass

class Product(Concept):
    def __init__(self, amount, tax) -> None:
        self.__amount = amount
        self.__tax = tax

    def description(self) -> str:
        return "Product"

    def price(self) -> float:
        return self.__amount + (self.__amount * self.__tax)

class Service(Concept):
    def __init__(self, amount) -> None:
        self.__amount = amount

    def description(self) -> str:
        return "Service"

    def price(self) -> float:
        return self.__amount

class ConceptFactory(ABC):
    def __init__(self, *args) -> None:
        self._args = args

    @abstractmethod
    def create(self) -> Concept:
        pass

class ProductFactory(ConceptFactory):
    def create(self) -> Concept:
        return Product(self._args[0], self._args[1])

class ServiceFactory(ConceptFactory):
    def create(self) -> Concept:
        return Service(self._args[0])

# This is part of polymorphism. Polymorphism is the behavior that an object can have depending on its context.
# The function does not know which object it will receive, but it knows that every object has the “description()” function.
def show_info(concept: Concept) -> None:
    print(f"This is a {concept.description()}.")

product_factory = ProductFactory(10, 0.16)
service_factory = ServiceFactory(20)

concept1 = product_factory.create()
concept2 = service_factory.create()

show_info(concept1)
show_info(concept2)

print(f"Price of concept1: {concept1.price()}")
print(f"Price of concept2: {concept2.price()}")
