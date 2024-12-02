def print_tree(n: int)->None:
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the pyramid: "))
    print_tree(n)
