# used compiler - https://www.onlinegdb.com/
# importing nessesacry library
import random

# 1 - amocana - using OOP approach


class BinaryToDecimal:
    def __init__(self):
        self.ten = 0
        self.times = 1

    def convert_number(self, n):

        while n > 0:
            leftover = n % 10
            n = n // 10
            self.ten += leftover * self.times
            self.times = self.times * 2

        print(self.ten)


n = int(1000)
BinaryToDecimal().convert_number(n)

# 2 - amocana - using OOP approach

s = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "car",
    "ball",
    "earth",
    "same",
    "damn",
)


class FilterTp:
    def __init__(self):
        self.newTp = ()

    def filter_tp(self, s):
        for index in s:
            if "a" and "b" in index:
                self.newTp = self.newTp + (index,)

        print(self.newTp)


FilterTp().filter_tp(s)

# 3 - amocana - using functionall approach

mesameFile = open("mesame_3.txt", "w")


def fill():
    kenti = ()
    luwi = ()
    samebi = ()
    for i in range(100):
        rnd = random.randrange(0, 10)
        if rnd % 2 == 0:
            luwi = luwi + (rnd,)
        elif rnd % 3 == 0:
            samebi = samebi + (rnd,)
        else:
            kenti = kenti + (rnd,)

    return luwi, kenti, samebi


print(fill())
mesameFile.write(str(fill()))
mesameFile.close()


# 4 - amocana - using functionall approach

f = open("meotxe_4.txt", "w")

tveebi = 3


def kurdghlebi(tveebi):
    n = (1, 1)
    for i in range(2, tveebi):
        n = n + (n[i - 1] + n[i - 2],)

    return "wyvili: ", n[tveebi - 1], "kurdgheli: ", n[tveebi - 1] * 2


print(kurdghlebi(tveebi))
f.write(str(kurdghlebi(tveebi)))
f.close()

# 5 - amocana  - using functionall approach


n = int(5)
randomRicxvi = random.randrange(0, 3)


def forFaq(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    print("in for loop:")
    print(f)


def whileFaq(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1

    print("in while: ")
    print(num)


def rekursiuliFaq(n):
    if n == 1 or n == 0:
        return 1
    else:
        # n! = n x (n - 1)!
        return n * rekursiuliFaq(n - 1)


if n < 0:
    print("factoriali uartyofiti ar sheidzleba , rom iyos")
else:
    if randomRicxvi == 0:
        forFaq(n)
    elif randomRicxvi == 1:
        whileFaq(n)
    elif randomRicxvi == 2:
        print("in recursive :")
        print(rekursiuliFaq(n))
    else:
        print("ver dagenenirda randomad ricxvi ")
