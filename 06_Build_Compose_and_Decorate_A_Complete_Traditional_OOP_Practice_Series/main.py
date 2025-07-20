# main.py

from classes import Weapon
from components.composer import Warrior
from components.decorator import FireEnchant, IceEnchant

# Make base weapon
sword = Weapon("Steel Sword", 50)

# Decorate weapon with fire
fire_sword = FireEnchant(sword)

# Create warrior with fire sword
warrior = Warrior("Eisha", fire_sword)

# Use decorated weapon
print(warrior.attack())
