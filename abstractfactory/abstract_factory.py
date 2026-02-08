from abc import ABC, abstractmethod
import random

# Product abstract class
class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

class Boss(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def special_attack(self):
        pass

class DesertEnemy(Enemy):
    def attack(self):
        print("Desert Enemy attacks with sandstorm! -5")

class WaterEnemy(Enemy):
    def attack(self):
        print("Water Enemy attacks with tidal wave! -5")

class DesertBoss(Boss):
    def attack(self):
        print("Desert Boss attacks with sandstorm! -10")

    def special_attack(self):
        print("Desert Boss uses sand tornado! -20")

class WaterBoss(Boss):
    def attack(self):
        print("Water Boss attacks with tidal wave! -10")

    def special_attack(self):
        print("Water Boss uses tsunami! -20")

# Factory abstract class
class EnemiesFactory(ABC):
    @abstractmethod
    def create_enemy(self) -> Enemy:
        pass

    @abstractmethod
    def create_boss(self) -> Boss:
        pass

class DesertEnemiesFactory(EnemiesFactory):
    def create_enemy(self) -> Enemy:
        return DesertEnemy()

    def create_boss(self) -> Boss:
        return DesertBoss()

class WaterEnemiesFactory(EnemiesFactory):
    def create_enemy(self) -> Enemy:
        return WaterEnemy()

    def create_boss(self) -> Boss:
        return WaterBoss()

class Game:
    def __init__(self, factory: EnemiesFactory):
        self.__factory = factory
        self.__enemy1 = self.__factory.create_enemy()
        self.__enemy2 = self.__factory.create_enemy()
        self.__boss = self.__factory.create_boss()

    def enemy_attack(self):
        # who_attack = random.choice([self.__enemy1, self.__enemy2, self.__boss])
        # who_attack.attack()
        who_attack = random.randint(1, 4)

        match who_attack:
            case 1:
                self.__enemy1.attack()
            case 2:
                self.__enemy2.attack()
            case 3:
                self.__boss.attack()
            case 4:
                self.__boss.special_attack()

# App 
# game = Game(WaterEnemiesFactory())
game = Game(DesertEnemiesFactory())
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()

