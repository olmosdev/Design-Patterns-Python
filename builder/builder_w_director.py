from abc import ABC, abstractmethod

class People:
    def __init__(self):
        self.name: str | None = None
        self.age: int | None = None
        self.country: str | None = None
        self.weight: float | None = None

    def __str__(self) -> str:
        return f"People(name={self.name}, age={self.age}, country={self.country}, weight={self.weight})"

# The class that is going to build People objects
class Builder(ABC):
    def set_name(self, name: str) -> None:
        pass

    def set_age(self, age: int) -> None:
        pass

    def set_country(self, country: str) -> None:
        pass

    def set_weight(self, weight: float) -> None:
        pass

class PeopleBuilder(Builder):
    def __init__(self):
        # Creating the blank object. In the "Builder" pattern, this is allowed, since the pattern is designed to build objects.
        self.__people = People()

    # Method Chaining Implementation
    def set_name(self, name: str) -> Builder:
        self.__people.name = name
        return self

    def set_age(self, age: int) -> Builder:
        self.__people.age = age
        return self
    
    def set_country(self, country: str) -> Builder:
        self.__people.country = country
        return self
    
    def set_weight(self, weight: float) -> Builder:
        self.__people.weight = weight
        return self

    def build(self) -> People:
        people = self.__people
        self.reset()
        return people

    def reset(self) -> None:
        self.__people = People()

class PeopleDirector:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def create_sophia(self) -> People:
        self.builder.set_name("Sophia").set_age(30).set_country("USA") # type: ignore
        return self.builder.build() # type: ignore

    def create_alexandra(self) -> People:
        self.builder.set_name("Alexandra").set_age(25).set_country("Canada").set_weight(60.5) # type: ignore
        return self.builder.build() # type: ignore

people_builder = PeopleBuilder()
# This is the advantage of the Builder pattern; you don't need to send all the elements that make up the product.
sophia = people_builder.set_name("Sophia").set_age(30).set_country("USA").build() # type: ignore
# print(sophia.__dict__)
print(sophia)

people_director = PeopleDirector(people_builder) 
sophia2 = people_director.create_sophia()
alexandra = people_director.create_alexandra()
print(sophia2)
print(alexandra)
