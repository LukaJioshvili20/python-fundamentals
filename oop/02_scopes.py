# from local scope edit class attributes
def update_health(amount: int):
    monster.health += amount


class Monster:
    def __init__(self, health, energy):
        self.health = health
        # self.energy = self.set_energy(energy)
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    # def set_energy(self, energy):
    #     new_energy = energy * 2
    #     return new_energy


# monster = Monster(100, 50)
# cleaner way to pass arguments
monster = Monster(health=100, energy=50)
# update class attribute outside its scope
# update_health(20)
print(monster.health, monster.energy)
