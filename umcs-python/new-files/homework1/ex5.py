# Using Python 3.13
# Using JetBrains PyCharm
# Luka Jioshvili

class ChristmasTree:
    def __init__(self):
        """Initializes the ChristmasTree with a default height of None."""

        self.height = None

    def _get_height(self) -> int:
        """Prompts the user for a natural number to set the tree height with validation.

        Returns:
            int: A positive integer representing the height of the Christmas tree.
        """

        while True:
            try:
                n = int(input("Enter a natural number for the height of the Christmas tree: "))
                if n > 0:
                    return n
                else:
                    print("Please enter a natural number greater than 0.")
            except ValueError:
                print("Invalid input! Please enter a natural number.")

    def _generate_tree_pattern(self) -> None:
        """Generates and prints the Christmas tree pattern based on the specified height."""

        for i in range(self.height):
            print(" " * (self.height - i - 1), end="")  # Print the spaces on the left
            print("/" * i, end="")  # Print the left slashes
            print("|", end="")  # Print the trunk part
            print("\\" * i)  # Print the right slashes

        print(" " * (self.height - 1) + "#")  # Print the tree base

    def display_tree(self) -> None:
        """Main method to generate and display the Christmas tree."""

        self.height = self._get_height()
        self._generate_tree_pattern()


if __name__ == '__main__':
    tree = ChristmasTree()
    tree.display_tree()
