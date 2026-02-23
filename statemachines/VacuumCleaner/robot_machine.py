from enum import Enum, auto

# Possible states of the robot
class RobotState(Enum):
    DOCKED = "DOCKED"      # In charging station
    CLEANING = "CLEANING"  # Working
    TRAPPED = "TRAPPED"    # Stuck with an obstacle
    LOW_BATTERY = "LOW_BATTERY"

# Events that trigger transitions
class RobotEvent(Enum):
    START = "START"
    OBSTACLE = "OBSTACLE"
    BATTERY_CRITICAL = "BATTERY_CRITICAL"
    HOME = "HOME"

# The transition map (The Machine)
machine = {
    RobotState.DOCKED: {
        RobotEvent.START: RobotState.CLEANING
    },
    RobotState.CLEANING: {
        RobotEvent.OBSTACLE: RobotState.TRAPPED,
        RobotEvent.BATTERY_CRITICAL: RobotState.LOW_BATTERY,
        RobotEvent.HOME: RobotState.DOCKED
    },
    RobotState.TRAPPED: {
        RobotEvent.START: RobotState.CLEANING # Resume after manual help
    },
    RobotState.LOW_BATTERY: {
        RobotEvent.HOME: RobotState.DOCKED
    }
}

def transition(current_state, event):
    if current_state not in machine:
        return current_state
    
    # Logic: Get next state or stay in current if event is invalid
    return machine[current_state].get(event, current_state)