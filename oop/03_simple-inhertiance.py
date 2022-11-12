class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount


class BossMonster(Monster):
    def __init__(self, special_damage, special_health, special_energy):
        super().__init__(health=special_health * 2, energy=special_energy * 3)
        self.special_damage = special_damage

    def special_attack(self):
        print(f"Ultra Combo with the damage: {self.special_damage}")


bossman = BossMonster(special_damage=44, special_health=300, special_energy=430)
print(bossman.health)
print(bossman.special_attack())
