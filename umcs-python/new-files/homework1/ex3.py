# Using Python 3.13
# Using JetBrains PyCharm
# Luka Jioshvili
def get_max_number() -> None:
    """Prompts the user to enter five numbers and displays the largest one.

    This function asks the user to input five integer numbers, then calculates
    and prints the maximum of these numbers.
    """
    print(max(int(input("Enter a number: ")) for _ in range(5)))


if __name__ == '__main__':
    get_max_number()
