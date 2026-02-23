import asyncio
from garage_controller import GarageController

async def bootstrap():
    garage = GarageController()
    
    print("--- Iniciando Sistema de Garaje ---")
    print(garage.get_info())

    # Simulación: Abrir la puerta
    await garage.press_remote_button()
    print(garage.get_info())

    # Simulación: Cerrar la puerta
    await garage.press_remote_button()
    print(garage.get_info())

if __name__ == "__main__":
    asyncio.run(bootstrap())