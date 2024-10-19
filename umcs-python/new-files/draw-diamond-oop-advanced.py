import curses
from dataclasses import dataclass, field
from typing import ClassVar, Callable, Dict
from colorama import Fore, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Define a global color map for reuse with numbered keys for easier selection
COLOR_MAP: Dict[int, str] = {
    1: Fore.YELLOW,
    2: Fore.GREEN,
    3: Fore.RED,
    4: Fore.BLUE,
    5: Fore.WHITE,
    6: Fore.CYAN,
    7: Fore.MAGENTA
}

COLOR_NAMES: Dict[int, str] = {
    1: 'Yellow',
    2: 'Green',
    3: 'Red',
    4: 'Blue',
    5: 'White',
    6: 'Cyan',
    7: 'Magenta'
}


class InvalidHeightError(Exception):
    """Custom exception for invalid height input."""
    pass


def validate_input(func: Callable) -> Callable:
    """Decorator for input validation."""

    def wrapper(self, *args, **kwargs) -> None:
        if self.height < 2:
            raise InvalidHeightError("Height must be at least 2.")
        return func(self, *args, **kwargs)

    return wrapper


def interactive_color_selection(stdscr, title: str) -> str:
    """
    Display an interactive menu for color selection, allowing the user to use arrow keys to select.

    Args:
        stdscr: The curses standard screen object.
        title (str): The prompt or title to display.

    Returns:
        str: The selected color escape code.
    """
    curses.curs_set(0)  # Hide the cursor
    current_selection = 0  # Index of the current selection

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title, curses.A_BOLD)

        # Display all color options
        for index, name in COLOR_NAMES.items():
            if current_selection == index - 1:
                # Highlight the current selection
                stdscr.addstr(index, 0, f"> {name}", curses.A_REVERSE)
            else:
                stdscr.addstr(index, 0, f"  {name}")

        # Get the user input
        key = stdscr.getch()

        # Handle key inputs
        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(COLOR_NAMES) - 1:
            current_selection += 1
        elif key == ord(' '):  # Space bar to select
            return COLOR_MAP[current_selection + 1]

        stdscr.refresh()


def get_user_input(stdscr, prompt: str, row: int = 0) -> str:
    """
    Get user input in the curses interface.

    Args:
        stdscr: The curses standard screen object.
        prompt (str): The prompt to display to the user.
        row (int): The row on the screen where the input prompt will be displayed.

    Returns:
        str: The user's input.
    """
    stdscr.clear()
    stdscr.addstr(row, 0, prompt)
    stdscr.refresh()

    curses.echo()  # Enable echo so the user can see what they are typing
    user_input = stdscr.getstr(row + 1, 0).decode('utf-8')  # Get the user's input
    curses.noecho()  # Disable echo after input

    return user_input


@dataclass
class Diamond:
    """
    A class to represent a Diamond shape pattern with configurable character, spacing, and colors.

    Attributes:
        height (int): The height of the diamond (number of rows for the top half).
        char (str): The character used to draw the diamond.
        space_char (str): The character used for spacing around the diamond.
        char_color (str): The color for the diamond character.
        space_color (str): The color for the spacing character.
    """
    height: int
    char: str = '*'
    space_char: str = ' '
    char_color: str = field(default=Fore.YELLOW)  # Default color for the diamond
    space_color: str = field(default=Fore.WHITE)  # Default color for the spacing
    MAX_HEIGHT: ClassVar[int] = 50  # Optional, you can set a max height limit

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if self.height > self.MAX_HEIGHT:
            raise ValueError(f"Height must be less than or equal to {self.MAX_HEIGHT}.")

    @validate_input
    def draw(self) -> None:
        """Draws the full diamond pattern with color."""
        print(self._generate_top())
        print(self._generate_bottom())

    def _generate_top(self) -> str:
        """Generates the top half of the diamond including the middle row."""
        top_half: list[str] = []
        for i in range(self.height):
            spaces = self.space_color + self.space_char * (self.height - i - 1)
            stars = self.char_color + self.char * (2 * i + 1)
            top_half.append(f"{spaces}{stars}{spaces}")
        return "\n".join(top_half)

    def _generate_bottom(self) -> str:
        """Generates the bottom half of the diamond excluding the middle row."""
        bottom_half: list[str] = []
        for i in range(self.height - 2, -1, -1):
            spaces = self.space_color + self.space_char * (self.height - i - 1)
            stars = self.char_color + self.char * (2 * i + 1)
            bottom_half.append(f"{spaces}{stars}{spaces}")
        return "\n".join(bottom_half)

    def __str__(self) -> str:
        """Custom string representation to directly print the diamond."""
        return self._generate_top() + "\n" + self._generate_bottom()


def main(stdscr):
    stdscr.clear()  # Ensure screen is cleared

    # Get inputs using the curses interface
    height_str = get_user_input(stdscr, "Enter the height of the diamond: ")
    height: int = int(height_str)

    char: str = get_user_input(stdscr, "Enter the character to draw the diamond (default '*'): ") or '*'
    space_char: str = get_user_input(stdscr, "Enter the character for spacing (default ' '): ") or ' '

    # Interactive color selection for diamond and spacing
    char_color: str = interactive_color_selection(stdscr, "Choose a color for the diamond:")
    space_color: str = interactive_color_selection(stdscr, "Choose a color for the spacing:")

    diamond = Diamond(height, char, space_char, char_color, space_color)

    # Display the diamond outside of curses
    stdscr.clear()
    stdscr.addstr(0, 0, f"Diamond drawn with height {height}.\n")
    stdscr.addstr(1, 0, f"Press any key to view the diamond in terminal...")
    stdscr.refresh()
    stdscr.getch()  # Wait for user input to proceed

    # Exit curses before printing the diamond
    curses.endwin()
    diamond.draw()  # Print the diamond in standard terminal output


if __name__ == "__main__":
    curses.wrapper(main)
