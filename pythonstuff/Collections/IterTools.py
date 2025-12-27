import itertools

print("== count() ==")

counter = itertools.count(start=10, step=5)# (10, 5)
for i in counter:
    if i > 20:
        break
    print(i, end=' ')
print("\n")

print()

print("== cycle() ==")

l = ['A', 'B', 'C']
cycler = itertools.cycle(l)
for i, letter in enumerate(cycler):
    print(i, letter, sep=": ")
    
    if i == 20:
        break

print()

print("== repeat() ==")

string = "String"
repeater = itertools.repeat(string, times=10)
print(repeater)
# print(list(repeater)) If we convert to list, we can't iterate again

for s in repeater:
    print(s)

print()

print("== accumulate() ==")
import operator

numbers = [1, 2, 3, 4, 5]
accumulation = itertools.accumulate(numbers) 
print(list(accumulation))

accumulation = itertools.accumulate(numbers, func=lambda x, y: x * y) 
print(list(accumulation))

accumulation = itertools.accumulate(numbers, operator.mul) 
print(list(accumulation))

print()

print("== chain() ==")

a = [1, 2, 3]
b = ['a', 'b', 'c']
combined = itertools.chain(a, b, a, b)
print(list(combined))

print()

print("== compress() ==")

l = ['a', 'b', 'c', 'd', 'e']
selectors = [0, 1, 1, 0, 1] # 0 = False, 1 = True
compressed = itertools.compress(l, selectors)
print(list(compressed))

print()

print("== dropwhile() ==")

l = [1, 2, 3, 4, 5, 6, 7, 1, 1, 2]
remeaning = itertools.dropwhile(lambda x: x < 3, l)
print(list(remeaning))

print()

print("== filterfalse() ==")

l = range(100)
filtered = itertools.filterfalse(lambda x: x % 10, l) # 0 == False
print(list(filtered))

l = [0, 1, False, True]
filtered = itertools.filterfalse(None, l)
print(list(filtered))

print()

print("== groupby() ==")

l = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('c', 5), ('c', 6)]
grouped = itertools.groupby(l, key=lambda k: k[0])
for key, values in grouped:
    print(key, list(values), sep=": ")

l = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2]
example = [list(g) for k, g in itertools.groupby(l)]
print(example)

print()

print("== islice() ==")

l = ['a', 'b', 'c', 'd', 'e', 'f']
sliced = itertools.islice(l, 2, None) # equals to [2:]. Even, we can remove "None" from the argumnets
print(list(sliced))

print()

print("== pairwise() ==")

l = "abcde" # To work with this, we need to elements at least. Otherwise, we'll going to get an empty iterator like []
paired = itertools.pairwise(l)
print(list(paired))

print()

print("== starmap() ==")
from operator import pow

l = [(2, 3), (2, 4), (2, 5)]
star_mapped = itertools.starmap(pow, l)
print(list(star_mapped))

l = [(1, 2, 3, 4), (4, 5), (6, 7)]
def example(*args):
    temp = []
    for arg in args:
        temp.append(f"{arg}X")
    return temp
star_mapped = itertools.starmap(example, l)
print(list(star_mapped))

print()

print("== takewhile() ==")

l = [1, 2, 3, 4, 5, 6, 1]
taken = itertools.takewhile(lambda a: a < 4, l)
print(list(taken))

print()

print("== tee() ==")

l = [1, 2, 3, 'a', 'b', 'c']
tee = itertools.tee(l, 3)
for it in tee:
    print(list(it))
    
print()

print("== zip_longest() ==")

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]
zipped = zip(a, b, c)
for a, b, c in zipped:
    print(a, b, c, sep=" : ")
print()

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]
zipped = itertools.zip_longest(a, b, c)
for a, b, c in zipped:
    print(a, b, c, sep=" : ")
print()

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]
zipped = itertools.zip_longest(a, b, c, fillvalue='X')
for a, b, c in zipped:
    print(a, b, c, sep=" : ")

print()

print("== product() ==")

a = [1, 2, 3]
b = ['a', 'b', 'c']
output = itertools.product(a, b)
for t in list(output):
    print(t)
print()

a = [1, 2, 3]
b = ['a', 'b', 'c']
output = itertools.product(a, b, repeat=2) # To build something like a Cartesian product
for t in list(output):
    print(t)

print()

print("== permutations() ==")

l = ['A', 'B', 'C']
permutations = itertools.permutations(l) # Or (l, 2)
for g in list(permutations):
    print(*g, sep=' ')
    print(g)
    print()

print()

print("== combinations() ==")
l = [0, 1, 2, 3]
combinations = itertools.combinations(l, 3)
for g in list(combinations):
    print(g)

print()

print("== combinations_with_replacement() ==")

l = [0, 1, 2, 3]
combinations = itertools.combinations_with_replacement(l, 3)
for g in list(combinations):
    print(g)

print()


