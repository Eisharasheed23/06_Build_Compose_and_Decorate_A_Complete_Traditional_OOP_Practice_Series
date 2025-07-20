# base/core_classes.py

class Character:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is a brave warrior."

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use(self):
        return f"Using {self.name} to deal {self.damage} damage."
