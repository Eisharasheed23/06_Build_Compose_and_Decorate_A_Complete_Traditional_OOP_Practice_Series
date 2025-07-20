# components/decorator.py

class WeaponDecorator:
    def __init__(self, weapon):
        self.weapon = weapon

    def use(self):
        return self.weapon.use()

class FireEnchant(WeaponDecorator):
    def use(self):
        return self.weapon.use() + " 🔥 Now it burns enemies!"

class IceEnchant(WeaponDecorator):
    def use(self):
        return self.weapon.use() + " ❄️ Now it freezes enemies!"
