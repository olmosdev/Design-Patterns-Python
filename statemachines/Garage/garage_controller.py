import asyncio
from garage_machine import DoorState, DoorEvent, transition

class GarageController:
    def __init__(self):
        self.state = DoorState.CLOSED

    async def press_remote_button(self):
        print(f"\n[Acción]: Botón presionado. Estado actual: {self.state.value}")
        self.state = transition(self.state, DoorEvent.PRESS_BUTTON)
        
        if self.state == DoorState.OPENING:
            await self._move_door("Abriendo")
            self.state = transition(self.state, DoorEvent.SENSOR_FULLY_OPEN)
        elif self.state == DoorState.CLOSING:
            await self._move_door("Cerrando")
            self.state = transition(self.state, DoorEvent.SENSOR_FULLY_CLOSED)

    async def _move_door(self, action):
        print(f"-> [Motor]: {action} puerta...")
        await asyncio.sleep(1.5) # Simula el tiempo que tarda en moverse
        print(f"-> [Sensor]: Límite alcanzado.")

    def get_info(self):
        return f"Estado de la Puerta: {self.state.value}"