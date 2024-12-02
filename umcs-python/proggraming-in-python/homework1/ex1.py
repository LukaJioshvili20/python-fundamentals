# Using Python 3.13
# Using JetBrains PyCharm
# Luka Jioshvili

from typing import List


class NumberListSorter:
    def __init__(self) -> None:
        """Initializes NumberSorter with an empty list for numbers."""

        self._numbers: List[int] = []

    def _get_integer(self, prompt: str) -> int:
        """Prompts the user for a single integer input with validation.

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

    def _collect_numbers(self) -> None:
        """Collects three integers from the user and stores them in the numbers list."""

        for i in range(3):
            num = self._get_integer(f"Enter integer {i + 1}: ")
            self._numbers.append(num)

    def _quick_sort(self, arr: List[int]) -> List[int]:
        """Sorts a list of integers using the quick sort algorithm.

        Args:
            arr (List[int]): The list of integers to sort.

        Returns:
            List[int]: A new list with integers sorted in ascending order.
        """

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self._quick_sort(left) + middle + self._quick_sort(right)

    def _sort_numbers(self) -> List[int]:
        """Sorts the collected numbers in ascending order.

        something here
                Returns:
                    List[int]: The sorted list of numbers.
        """

        self._numbers = self._quick_sort(self._numbers)
        return self._numbers

    def display_sorted_numbers(self) -> None:
        """Display the sorted list of numbers."""

        self._collect_numbers()
        sorted_numbers = self._sort_numbers()
        print("Numbers in ascending order:", sorted_numbers)


if __name__ == "__main__":
    sorter = NumberListSorter()
    sorter.display_sorted_numbers()
