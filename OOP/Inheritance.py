class People:

    classname = "people" # public field

    def __init__(self, my_name: str, is_married: bool) -> None:
        self.my_name = my_name # Public encapsulation
        self.__is_married = is_married # Private field

    def hi(self, name: str) -> None:
        print("Hi there! This is {1}. How are you, {0}?".format(name, self.my_name))

    def bye(self) -> None:
        print("Bye bye!")

    # Private encapsulation
    def get_is_married(self) -> bool:
        return self.__is_married

    def __some(self):
        print("Some")

    @staticmethod # we use this decorator when we don't need to access to anything
    def secret_message():
        print("I'm 17")

    @classmethod # cls allows us to access to the class elements
    def another_secret_message(cls): # "self" is the object and "cls" is the class
        print("I don't like pizza with pineapple")


class Barman(People):
    pass # To preserve the original constructor

    def welcome(self) -> None:
        print("Welcome!")

    def bye(self) -> None:
        print("Come back soon!")

class Student(People):
    def __init__(self, my_name: str, is_married: bool, profession: str) -> None:
        super().__init__(my_name, is_married)
        self.profession = profession

    # Method overriding
    def hi(self):
        print(f"Hello! This is {self.my_name}. I'm a {self.profession}")

    def bye(self) -> None:
        print("See you later!")

# To see polymorphism
def show(people) -> None:
    people.bye()

hector = Barman("Hector", False)
hector.hi("Lola")
hector.another_secret_message()
print(hector.get_is_married()) 
hector.welcome()
# hector.__some() Subclasses do not inherit private fields or methods, therefore this method will not display anything.

lupita = Student("Lupita", False, "Software Engineer")
lupita.hi()
lupita.another_secret_message()
print(lupita.get_is_married()) 

pepe = People("Pepe", False)

show(pepe)
show(hector)
show(lupita)