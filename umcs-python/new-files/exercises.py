import random


class Exercise1:
    """
    A number guessing game where the user picks a range, and the program selects a random number
    within that range. The user must guess the number with guidance on whether to go higher or lower.

    Attributes:
        min_value (int): The lower bound of the random number range.
        max_value (int): The upper bound of the random number range.
        _target_number (int): The randomly selected number within the range, which the user tries to guess.
    """

    def __init__(self):
        """
        Initializes the game by asking the user for the minimum and maximum values for the number range,
        and generates a random target number within that range.
        """
        self.min_value = self._get_min_value()
        self.max_value = self._get_max_value()
        self._target_number = random.randint(self.min_value, self.max_value)

        # Trigger Guessing Loop
        self._guess_the_number()

    def _get_min_value(self) -> int:
        """
        Prompts the user for the minimum value of the range.

        Returns:
            int: The user-provided minimum value.
        """
        while True:
            try:
                return int(input("Enter the minimum value for the range: "))
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def _get_max_value(self) -> int:
        """
        Prompts the user for the maximum value of the range, ensuring it is greater than the minimum value.

        Returns:
            int: The user-provided maximum value.
        """
        while True:
            try:
                max_value = int(input("Enter the maximum value for the range: "))
                if max_value <= self.min_value:
                    print(f"Maximum value must be greater than {self.min_value}.")
                else:
                    return max_value
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def _get_valid_input(self) -> int:
        """
        Prompts the user to guess a number within the selected range, ensuring valid input.

        Returns:
            int: The user-provided guess.
        """
        while True:
            try:
                return int(
                    input(
                        f"Guess the number (between {self.min_value} and {self.max_value}): "
                    )
                )
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def _guess_the_number(self) -> None:
        """
        Main game loop where the user guesses the target number.
        Provides feedback on whether to guess higher or lower, and ends when the correct number is guessed.
        """
        user_has_guessed: bool = False

        while not user_has_guessed:
            number = self._get_valid_input()

            if number < self._target_number:
                print("Go Higher")
            elif number > self._target_number:
                print("Go Lower")
            else:
                user_has_guessed = True
                print(f"Congratulations! You've guessed the correct number: {number}")


if __name__ == "__main__":
    try:
        game = Exercise1()
    except ValueError as e:
        print(f"Error: {e}")
