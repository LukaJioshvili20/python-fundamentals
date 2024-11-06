# Using Python 3.13
# Using JetBrains PyCharm
# Luka Jioshvili
import math
from typing import Union


class PrimeChecker:
    def __init__(self) -> None:
        """Initializes PrimeChecker with a placeholder for the number to check."""

        self._number: Union[int, None] = None

    def _get_integer(self, prompt: str) -> int:
        """Prompts the user for an integer input with validation.

        Args:
            prompt (str): The prompt message for the input.

        Returns:
            int: The integer entered by the user.
        """

        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def _is_prime(self, n: int) -> bool:
        """Determines if a given number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if n is prime, False otherwise.
        """

        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    def check_prime(self) -> None:
        """Gets a number from the user, checks if it's prime, and prints the result."""
        
        self._number = self._get_integer("Enter a number to check if it's prime: ")
        if self._is_prime(self._number):
            print(f"{self._number} is a prime number.")
        else:
            print(f"{self._number} is not a prime number.")


if __name__ == '__main__':
    prime_checker = PrimeChecker()
    prime_checker.check_prime()
