class Diamond:
    """
    A class used to represent a Diamond shape pattern.

    Attributes:
        height (int): The height of the diamond (number of rows for the top half).
        char (str): The character used to draw the diamond.
        space_char (str): The character used for spacing around the diamond.
    """

    def __init__(self, height: int, char: str = '*', space_char: str = ' '):
        """
        Constructs all the necessary attributes for the Diamond object.

        Args:
            height (int): The height of the diamond. Must be greater than or equal to 2.
            char (str, optional): The character used to draw the diamond. Defaults to '*'.
            space_char (str, optional): The character used for spacing. Defaults to ' '.

        Raises:
            ValueError: If height is less than 2.
        """
        if height < 2:
            raise ValueError("Height must be at least 2.")
        self.height = height
        self.char = char
        self.space_char = space_char

    def draw(self) -> None:
        """
        Draws the diamond pattern by calling internal methods to draw the top and bottom halves.
        """
        self._draw_top()
        self._draw_bottom()

    def _draw_top(self) -> None:
        """
        Draws the top half of the diamond pattern including the middle row.
        """
        for i in range(self.height):
            spaces = self.space_char * (self.height - i - 1)
            stars = self.char * (2 * i + 1)
            print(spaces + stars + spaces)

    def _draw_bottom(self) -> None:
        """
        Draws the bottom half of the diamond pattern, excluding the middle row.
        """
        for i in range(self.height - 2, -1, -1):
            spaces = self.space_char * (self.height - i - 1)
            stars = self.char * (2 * i + 1)
            print(spaces + stars + spaces)


if __name__ == "__main__":
    try:
        height = int(input("Enter the height of the diamond: "))
        char = input("Enter the character to draw the diamond (default '*'): ") or '*'
        space_char = input("Enter the character for spacing (default ' '): ") or ' '
        diamond = Diamond(height, char, space_char)
        diamond.draw()
    except ValueError as e:
        print(e)
