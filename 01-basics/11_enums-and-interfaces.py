from enum import Enum, auto


class CustomColor(Enum):
    RED = "#Witeli"


if __name__ == "__main__":
    print("Hello enums")

    print(CustomColor.RED)
    print(CustomColor.RED.value)
    # print(CustomColor.RED.name)
