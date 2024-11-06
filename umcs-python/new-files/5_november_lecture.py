def test() -> None:
    print('Hello')


def div(a, b):
    if b == 0:
        print('dIVVSION BY 0')
        return None

    return a / b


def div_oneliner(a: float, b: float) -> float | None:
    return a / b if b != 0 else None


def calculate_number_of_a(word: str) -> int:
    if len(word) > 0:
        return word.count("a")

    return 0


DEFAULT_LIST: [int] = [503, 1, 4, 3, 6, 73, 301]

if __name__ == "__main__":
    test()
    calculate_number_of_a('Luka a a')
    print(f"max is : {max(DEFAULT_LIST)}")
