def add(*args) -> int:
    total = 0
    for number in args:
        total +=  number

    return total

res1 = add(1, 2, 3)
print(f"Result: {res1}")