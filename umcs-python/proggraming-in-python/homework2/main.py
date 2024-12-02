from typing import List, Tuple
import time

CellState = int
Neighborhood = Tuple[CellState, CellState, CellState]
RuleTable = dict[Neighborhood, CellState]


class CellularAutomaton:
    """
    A class to represent an elementary cellular automaton for any rule.

    This automaton evolves a 1D grid of cells based on the specified rule's neighborhood logic.

    Attributes:
        width (int): The number of cells in the grid.
        generations (int): The number of generations to simulate.
        rule (int): The rule number (0-255) defining the automaton's behavior.
        grid (List[List[CellState]]): The grid storing all generations of the automaton.
        rule_table (RuleTable): A dictionary defining transitions for the specified rule.
    """

    def __init__(self) -> None:
        """
        Initializes the CellularAutomaton by gathering user input for width, generations, and rule.
        """

        self.width, self.generations, self.rule = self._get_user_input()
        self.grid: List[List[CellState]] = []
        self.rule_table: RuleTable = self._create_rule_table()

    def _get_user_input(self) -> Neighborhood:
        """
        Prompts the user for input to configure the automaton.

        Returns:
            Tuple[int, int, int]: The grid width, number of generations, and rule number.
        """

        try:
            width: int = int(input("Enter grid width (e.g., 31): "))
            generations: int = int(input("Enter number of generations (e.g., 15): "))
            rule: int = int(input("Enter rule number (0-255): "))

            if not 0 <= rule <= 255:
                raise ValueError("Rule number must be between 0 and 255.")

            return width, generations, rule
        except ValueError as e:
            print(f"Invalid input: {e}")
            return self._get_user_input()

    def _create_rule_table(self) -> RuleTable:
        """
        Creates the transition table based on the rule number.

        Returns:
            RuleTable: A dictionary mapping neighborhoods to their next state.
        """

        binary_rule = f"{self.rule:08b}"
        neighborhoods = [
            (1, 1, 1),
            (1, 1, 0),
            (1, 0, 1),
            (1, 0, 0),
            (0, 1, 1),
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        ]

        rule_table = {}
        for i in range(len(neighborhoods)):
            neighborhood = neighborhoods[i]
            state = int(binary_rule[i])
            rule_table[neighborhood] = state

        return rule_table

    def _initialize_grid(self) -> None:
        """
        Initializes the grid with a single active cell in the center.
        """

        half_width: int = self.width // 2

        left_padding: List[CellState] = [0] * half_width
        center_cell: List[CellState] = [1]
        right_padding: List[CellState] = [0] * half_width

        initial_state: List[CellState] = left_padding + center_cell + right_padding
        self.grid.append(initial_state)

    def _compute_next_generation(
        self, current_state: List[CellState]
    ) -> List[CellState]:
        """
        Computes the next generation of cells based on the current state.

        Args:
            current_state (List[CellState]): The current generation of cells.

        Returns:
            List[CellState]: The next generation of cells.
        """

        next_state: List[CellState] = []
        for i in range(self.width):
            left: CellState = current_state[i - 1] if i > 0 else 0
            center: CellState = current_state[i]
            right: CellState = current_state[i + 1] if i < self.width - 1 else 0
            neighborhood: Neighborhood = (left, center, right)
            next_state.append(self.rule_table[neighborhood])
        return next_state

    def generate(self) -> None:
        """
        Simulates the automaton for the specified number of generations.

        This method initializes the grid and calculates all subsequent generations.
        """

        self._initialize_grid()
        for _ in range(self.generations):
            current_state: List[CellState] = self.grid[-1]
            next_state: List[CellState] = self._compute_next_generation(current_state)
            self.grid.append(next_state)

    def display(self) -> None:
        """
        Displays the automaton grid in a human-readable format.

        Active cells are represented by '|', and inactive cells are represented by spaces.
        """

        for row in self.grid:
            row_str: str = self._convert_row_to_string(row)
            print(row_str)

    def _convert_row_to_string(self, row: List[CellState]) -> str:
        """
        Converts a row of cells into a displayable string.

        Args:
            row (List[CellState]): A list of cell states (0 or 1).

        Returns:
            str: A string representation of the row where 1 is '|' and 0 is a space.
        """

        result: str = ""
        for cell in row:
            if cell == 1:
                result += "|"
            else:
                result += " "
        return result

    def get_grid(self) -> List[List[CellState]]:
        """
        Returns the computed grid.
        """

        return self.grid


class AutomatonSimulator:
    """
    A class to simulate the drawing of a CellularAutomaton.
    """

    def __init__(self, grid: List[List[CellState]]) -> None:
        """
        Initializes the simulator with the automaton's grid.

        Args:
            grid (List[List[CellState]]): The computed grid of the automaton.
        """

        self.grid = grid

    def simulate(self, delay: float = 0.3) -> None:
        """
        Simulates the drawing of the automaton grid line by line.

        Args:
            delay (float): The time delay (in seconds) between drawing each line.
        """

        for row in self.grid:
            print(self._convert_row_to_string(row))
            time.sleep(delay)

    def _convert_row_to_string(self, row: List[CellState]) -> str:
        """
        Converts a row of cells into a displayable string.

        Args:
            row (List[CellState]): A list of cell states (0 or 1).

        Returns:
            str: A string representation of the row where 1 is '|' and 0 is a space.
        """

        return "".join("|" if cell == 1 else " " for cell in row)


if __name__ == "__main__":
    automaton = CellularAutomaton()
    automaton.generate()
    # automaton.display()

    simulator = AutomatonSimulator(automaton.get_grid())
    simulator.simulate(delay=0.5)
