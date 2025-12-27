class Singleton:
    _instance = None # _<variable_name> = protected, __<variable_name> = privated

    def __new__(cls, name = None, age = None):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            # At this point, "_instance" is an object, not a class
            # Adding new fields to the object
            cls._instance.name = name
            cls._instance.age = age
        return cls._instance

singleton1 = Singleton("Ariana", "27")
singleton2 = Singleton("Isabel", 30) # This object should not exist.
singleton3 = Singleton()

print(singleton1 is singleton2) # Are the same object?
print(singleton1.name)
print(singleton2.name)
print(singleton3.name)