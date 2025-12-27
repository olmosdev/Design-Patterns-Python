import json
from typing_extensions import Self 

class ConfigSingleton:
    _instance = None

    def __new__(cls, file_name = "config.json"):
        if not cls._instance:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            cls._instance.__load(file_name)
        return cls._instance
    
    def __load(self, file_name):
        try:
            with open(file_name, "r") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = None
            print("File not found")
        except json.JSONDecodeError:
            self.config = None
            print("Invalid format in JSON file")

    def get(self, key):
        return self.config.get(key, "None")

config1 = ConfigSingleton("config.json")
print(config1.get("version"))
print(config1.get("name"))
print(config1.get("ola"))

config2 = ConfigSingleton()
print(config2 is config1)
print(config2.get("version"))
print(config2.get("name"))
print(config2.get("ola"))
