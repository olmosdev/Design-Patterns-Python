import asyncio
from vacuum_cleaner import VacuumCleaner

async def bootstrap():
    my_robot = VacuumCleaner()

    print("--- Robot Mission Start ---")
    await my_robot.start_mission()

    # The robot is trapped, we help it manually
    my_robot.manual_release()

    print(f"\nFinal Status: {my_robot.get_status()}")

if __name__ == "__main__":
    asyncio.run(bootstrap())