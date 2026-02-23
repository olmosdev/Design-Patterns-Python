from enum import Enum

class DoorState(Enum):
    CLOSED = "CLOSED"
    OPENING = "OPENING"
    OPEN = "OPEN"
    CLOSING = "CLOSING"
    STOPPED = "STOPPED" 

class DoorEvent(Enum):
    PRESS_BUTTON = "PRESS_BUTTON"
    SENSOR_FULLY_OPEN = "SENSOR_FULLY_OPEN"
    SENSOR_FULLY_CLOSED = "SENSOR_FULLY_CLOSED"
    OBSTACLE_DETECTED = "OBSTACLE_DETECTED"

machine = {
    DoorState.CLOSED: {
        DoorEvent.PRESS_BUTTON: DoorState.OPENING
    },
    DoorState.OPENING: {
        DoorEvent.SENSOR_FULLY_OPEN: DoorState.OPEN,
        DoorEvent.OBSTACLE_DETECTED: DoorState.STOPPED
    },
    DoorState.OPEN: {
        DoorEvent.PRESS_BUTTON: DoorState.CLOSING
    },
    DoorState.CLOSING: {
        DoorEvent.SENSOR_FULLY_CLOSED: DoorState.CLOSED,
        DoorEvent.OBSTACLE_DETECTED: DoorState.STOPPED
    },
    DoorState.STOPPED: {
        DoorEvent.PRESS_BUTTON: DoorState.OPENING # Reintentar abrir
    }
}

def transition(current_state, event):
    if current_state not in machine:
        return current_state
    
    return machine[current_state].get(event, current_state)