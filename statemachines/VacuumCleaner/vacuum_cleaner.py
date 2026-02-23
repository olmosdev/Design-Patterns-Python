import asyncio
from robot_machine import RobotState, RobotEvent, transition

class VacuumCleaner:
    def __init__(self):
        self.state = RobotState.DOCKED

    async def start_mission(self):
        print(f"Current State: {self.state}")
        
        # 1. Start cleaning
        self.state = transition(self.state, RobotEvent.START)
        print("-> [Robot]: Cleaning the living room...")
        await asyncio.sleep(1)

        # 2. Simulate hitting a chair (Obstacle)
        self.state = transition(self.state, RobotEvent.OBSTACLE)
        print("-> [ALERT]: I'm trapped! Please help.")
        
    def manual_release(self):
        """Action triggered by a human to unstick the robot"""
        print("\n[Human]: Helping the robot...")
        self.state = transition(self.state, RobotEvent.START)
        print(f"-> [Robot]: New state: {self.state}")

    def get_status(self):
        return self.state