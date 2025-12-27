# Iterable (lists, tuples, strings)

my_string = "banana"
my_iter_s = iter(my_string)
print(type(my_iter_s))
print(next(my_iter_s))
print(next(my_iter_s))
print(next(my_iter_s))

for x in my_string:
    print(x)
    
my_list = ["apple", "banana", "cherry"]
my_iter_l = iter(my_list)
print(type(my_iter_l))
print(next(my_iter_l))
print(next(my_iter_l))
print(next(my_iter_l))

my_tuple = ("apple", "banana", "cherry")
my_iter_t = iter(my_tuple)
print(type(my_iter_t))
print(next(my_iter_t))
print(next(my_iter_t))
print(next(my_iter_t))

# Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print(type(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)
