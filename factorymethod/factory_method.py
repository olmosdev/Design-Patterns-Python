from abc import ABC, abstractmethod

class Concept(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

class Product(Concept):
    def description(self) -> str:
        return "Product"

class Service(Concept):
    def description(self) -> str:
        return "Service"

class ConceptFactory(ABC):
    @abstractmethod
    def create(self) -> Concept:
        pass

class ProductFactory(ConceptFactory):
    def create(self) -> Concept:
        return Product()

class ServiceFactory(ConceptFactory):
    def create(self) -> Concept:
        return Service()

# This is part of polymorphism. Polymorphism is the behavior that an object can have depending on its context.
# The function does not know which object it will receive, but it knows that every object has the “description()” function.
def show_info(concept: Concept) -> None:
    print(f"This is a {concept.description()}.")

product_factory = ProductFactory()
service_factory = ServiceFactory()

concept1 = product_factory.create()
concept2 = service_factory.create()

show_info(concept1)
show_info(concept2)
