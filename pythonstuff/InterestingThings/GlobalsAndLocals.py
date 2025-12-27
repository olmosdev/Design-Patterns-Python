x = 10
y = 20

def demo(a, b):
    c = a + b

    print("=== VARIABLES LOCALES ===")
    for nombre, valor in locals().items():
        print(f"{nombre}: {valor} (local)")

    print("\n=== VARIABLES GLOBALES ===")
    for nombre, valor in globals().items():
        # Filtramos solo variables definidas por nosotros
        if nombre in ("x", "y"):
            print(f"{nombre}: {valor} (global)")

demo(3, 4)
