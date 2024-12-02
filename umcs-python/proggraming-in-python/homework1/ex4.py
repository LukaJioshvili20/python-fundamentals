# Using Python 3.13
# Using JetBrains PyCharm
# Luka Jioshvili

from typing import List


class DivisibleFinder:
    def __init__(self):
        """Initializes DivisibleFinder without requiring any initial arguments."""

        self._n = None

    def _get_positive_integer(self) -> int:
        """Prompts the user for a positive integer with input validation.

        Returns:
            int: A positive integer entered by the user.
        """

        while True:
            try:
                n = int(input("Enter a positive integer: "))
                if n > 0:
                    return n
                else:
                    print("Please enter a positive integer greater than 0.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def _find_divisible_by_3_and_7(self) -> List[int]:
        """Finds numbers in the range from 1 to n that are divisible by both 3 and 7.

        Returns:
            List[int]: A list of integers from 1 to n divisible by both 3 and 7.
        """

        divisible_numbers: List[int] = []
        for num in range(1, self._n + 1):
            if num % 3 == 0 and num % 7 == 0:
                divisible_numbers.append(num)

        return divisible_numbers

    def display_divisible_numbers(self) -> None:
        """Collects input, processes it, and displays numbers divisible by 3 and 7."""

        self._n = self._get_positive_integer()
        divisible_numbers = self._find_divisible_by_3_and_7()
        print("Numbers divisible by 3 and 7:", divisible_numbers)


if __name__ == '__main__':
    finder = DivisibleFinder()
    finder.display_divisible_numbers()
