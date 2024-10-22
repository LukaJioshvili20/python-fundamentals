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
        self.min_value = self.__get_min_value()
        self.max_value = self.__get_max_value()
        self._target_number = random.randint(self.min_value, self.max_value)

        # Trigger Guessing Loop
        self.__guess_the_number()

    def __get_min_value(self) -> int:
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

    def __get_max_value(self) -> int:
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

    def __get_valid_input(self) -> int:
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

    def __guess_the_number(self) -> None:
        """
        Main game loop where the user guesses the target number.
        Provides feedback on whether to guess higher or lower, and ends when the correct number is guessed.
        """
        user_has_guessed: bool = False

        while not user_has_guessed:
            number = self.__get_valid_input()

            if number < self._target_number:
                print("Go Higher")
            elif number > self._target_number:
                print("Go Lower")
            else:
                user_has_guessed = True
                print(f"Congratulations! You've guessed the correct number: {number}")


class Exercise2:
    """
    A class to calculate the factorial of a given positive integer,
    with input validation to handle edge cases like zero and negative numbers.

    Attributes:
        target_number (int): The number for which the factorial will be calculated.
        result (int): The calculated factorial result.
    """

    def __init__(self):
        """
        Initializes the class, prompts the user for a number, and calculates the factorial.
        """
        self.target_number: int = self._ask_for_number()
        self.result: int = 1

        # Trigger the calculation
        self._calculate()

    def _ask_for_number(self) -> int:
        """
        Prompts the user to input a number for the factorial calculation and validates the input.

        Returns:
            int: The validated input number from the user.
        """
        while True:
            try:
                num = int(
                    input(
                        "Please input a non-negative integer to calculate its factorial: "
                    )
                )
                if num < 0:
                    print(
                        "Factorial is not defined for negative numbers. Please enter a non-negative integer."
                    )
                else:
                    return num
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def _calculate(self) -> None:
        """
        Calculates the factorial of the `target_number` and stores the result in `self.result`.
        Handles special cases like the factorial of 0 (which is 1).
        """
        if self.target_number == 0:
            self.result = 1
        else:
            for i in reversed(range(1, self.target_number + 1)):
                self.result *= i

        print(f"The factorial of {self.target_number} is {self.result}")


if __name__ == "__main__":
    try:
        # Exercise1()
        Exercise2()

    except ValueError as e:
        print(f"Error: {e}")
