from classes import Weapon
from components.decorator import FireEnchant

def test_fire_enchant():
    sword = Weapon("Sword", 30)
    fire = FireEnchant(sword)
    assert "burns" in fire.use()
