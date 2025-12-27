class People:

    classname = "people" # public field

    def __init__(self, my_name: str, is_married: bool) -> None:
        self.my_name = my_name # Public encapsulation
        self.__is_married = is_married # Private field

    def hi(self, name: str) -> None:
        print("Hi there! This is {1}. How are you, {0}?".format(name, self.my_name))

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


nidia = People("Nidia", True)
nidia.hi("Pepe")

print(nidia.classname)
print(People.classname)

nidia.secret_message()
People.secret_message()

nidia.another_secret_message()
People.another_secret_message()

# print(nidia.__is_married) # Not permitted
print(nidia.get_is_married())
# nidia.__some() # Not permitted
