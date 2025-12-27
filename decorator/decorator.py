from abc import ABC, abstractmethod

class Taco(ABC):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def description(self):
        pass

class BasicTaco(Taco):
    def price(self):
        return 5
    
    def description(self):
        return "Taco "
    
class TacoDecorator(Taco):
    def __init__(self, taco: Taco) -> None:
        self._taco = taco # _ = protected, __ = private

    # This method is never executed, but it was written to fulfill the contract.
    def price(self):
        return self._taco.price()

    # This method is never executed, but it was written to fulfill the contract.
    # But unlike the other method, to execute this function, we use super().
    def description(self):
        return self._taco.description() + "extra "

class DoubleMeatTaco(TacoDecorator):
    def price(self):
        return self._taco.price() + 4
    
    def description(self):
        return super().description() + "Double Meat "
    
class CheeseTaco(TacoDecorator):
    def price(self):
        return self._taco.price() + 2

    def description(self):
        return super().description() + "Cheese "
    
basic_taco = BasicTaco()
print(f"{basic_taco.description()} - ${basic_taco.price()}")
double_meat_taco = DoubleMeatTaco(basic_taco)
print(f"{double_meat_taco.description()} - ${double_meat_taco.price()}")
cheese_taco = CheeseTaco(double_meat_taco)
print(f"{cheese_taco.description()} - ${cheese_taco.price()}")
double_cheese_taco = CheeseTaco(cheese_taco)
print(f"{double_cheese_taco.description()} - ${double_cheese_taco.price()}")
