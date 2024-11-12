# "dunders" -  certain operations that are invoked by special syntax
class Jordans:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def __len__(self):
        return self.size

    def __abs__(self):
        return self.price

    # when class is created __call__ function is called
    def __call__(self):
        return "Brother come on"

    def __add__(self, other):
        return self.price + other

    def __str__(self):
        return f"What the hell, look at those {self.size} size \"Jordan's\""

    def roast_them_shoes(self, roast_string):
        print("What the hell")
        print(f"SLV: {roast_string}")
        Jordans.price = 0.08
        print(self.price)

    def say_three_things(self, things):
        for i in things:
            print(things[i])
        print("Tararararraaa")


jordans_01 = Jordans(7, 41)
print(jordans_01 + 30)
print(jordans_01)
