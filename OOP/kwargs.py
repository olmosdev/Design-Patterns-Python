def show(**kwargs) -> None:
    for key, value in kwargs.items():
        print(f"{key} - {value}")

show(name="Sophia", country="New Zeland")
