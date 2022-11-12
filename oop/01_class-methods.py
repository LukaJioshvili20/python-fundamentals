# pass function to class objects
def add(a: int, b: int) -> int:
    return a + b


class WhatTheHell:
    def __init__(self, add_function):
        self.add_function = add_function


what_the_hell = WhatTheHell(add_function=add)
print(what_the_hell.add_function(30, 20))


class Player:
    def __init__(self, func):
        self.func = func


class Attacks:
    def bite(self):
        print("bite")

    def strike(self):
        print("strike")

    def slash(self):
        print("slash")

    def kick(self):
        print("kick")


# return object of the class Attacks
attacks = Attacks()
player = Player(func=attacks.kick)
player.func()
