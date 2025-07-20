# components/composer.py

from classes import Character, Weapon

class Warrior:
    def __init__(self, name, weapon):
        self.character = Character(name)
        self.weapon = weapon

    def attack(self):
        desc = self.character.describe()
        weapon_action = self.weapon.use()
        return f"{desc} {weapon_action}"
