import math
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
        self.target_number: int = self.__ask_for_number()
        self.result: int = 1

        # Trigger the calculation
        self.__calculate()

    def __ask_for_number(self) -> int:
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

    def __calculate(self) -> None:
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


class Exercise3:
    def __init__(self):
        self.total_number_of_target_chars: int = 0
        self.target_char: str = ""
        self.target_string: str = ""

        self.__ask_for_target_string()
        self.__ask_for_target_char()

        self.__find_char_in_string()

    def __ask_for_target_char(self) -> None:
        while True:
            try:
                user_input_char = input("Enter a letter to search: ")
                if len(user_input_char) > 1 or len(user_input_char) == 0:
                    print("Please enter a only single letter.")
                else:
                    self.target_char = user_input_char
                    return
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def __ask_for_target_string(self) -> None:
        self.target_string = input("Enter word: ")

    def __find_char_in_string(
        self,
    ) -> None:
        for i in range(len(self.target_string)):
            if self.target_string[i] == self.target_char:
                self.total_number_of_target_chars += 1

        print(
            f"Count of letter {self.target_char} in word {self.target_string} is {self.total_number_of_target_chars}"
        )


class Exercise4:
    """
    A class to calculate the roots of a quadratic equation in the form ax^2 + bx + c = 0.

    Attributes:
        a (float): The coefficient of x^2.
        b (float): The coefficient of x.
        c (float): The constant term.
    """

    def __init__(self):
        """
        Initializes the class by asking the user for coefficients a, b, and c,
        and then calculates the roots of the quadratic equation.
        """
        self.a = self._get_coefficient("a")
        self.b = self._get_coefficient("b")
        self.c = self._get_coefficient("c")
        self._calculate_roots()

    def _get_coefficient(self, name: str) -> float:
        """
        Prompts the user to input a valid coefficient.

        Args:
            name (str): The name of the coefficient (e.g., 'a', 'b', 'c').

        Returns:
            float: The user-provided coefficient.
        """
        while True:
            try:
                return float(input(f"Enter coefficient {name}: "))
            except ValueError:
                print(
                    f"Invalid input! Please enter a valid number for coefficient {name}."
                )

    def _calculate_roots(self) -> None:
        """
        Calculates the roots of the quadratic equation based on the discriminant.
        Prints the result based on whether the equation has two real roots, one double root, or no real roots.
        """
        discriminant = self.b**2 - 4 * self.a * self.c

        if self.a == 0:
            print("The value of 'a' should not be zero for a quadratic equation.")
            return

        if discriminant > 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            print(f"The equation has two real roots: {root1} and {root2}")

        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            print(f"The equation has one double root: {root}")

        else:
            print("The equation has no real roots.")


class Exercise5:
    """
    A class that asks the user to input 5 numbers and finds the largest number using a for loop.

    Attributes:
        numbers (list of float): A list of 5 user-provided numbers.
        largest_number (float): The largest number from the input list.
    """

    def __init__(self):
        """
        Initializes the class, asks for user input, and finds the largest number.
        """
        self.numbers = []
        self.largest_number = None
        self._get_numbers_from_user()
        self._find_largest_number()

    def _get_numbers_from_user(self) -> None:
        """
        Prompts the user to input 5 numbers and stores them in the `numbers` list.
        """
        for i in range(5):
            while True:
                try:
                    number = float(input(f"Enter number {i + 1}: "))
                    self.numbers.append(number)
                    break  # Exit the loop if the input is valid
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

    def _find_largest_number(self) -> None:
        """
        Finds the largest number from the list of numbers entered by the user.
        """
        for number in self.numbers:
            if self.largest_number is None or number > self.largest_number:
                self.largest_number = number

        print(f"The largest number is: {self.largest_number}")


if __name__ == "__main__":
    try:
        print("Welcome to Exercise1!")
        Exercise1()
        print("Welcome to Exercise2!")
        Exercise2()
        print("Welcome to Exercise3!")
        Exercise3()
        print("Welcome to Exercise4!")
        Exercise4()
        print("Welcome to Exercise5!")
        Exercise5()
    except ValueError as e:
        print(f"Error: {e}")
