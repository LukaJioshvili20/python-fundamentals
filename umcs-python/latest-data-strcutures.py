import bisect
import cProfile
import time
from collections import ChainMap
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple

""" To customize behavior of dictionary, list, and string"""
# from collections import UserDict
# from collections import UserList
# from collections import UserString


from enum import StrEnum


def process_large_data():
    data = list(range(1, 1000000))  # 1 million items
    result = [x * 2 for x in data if x % 2 == 0]  # Example operation


def process_command(command):
    match command:
        case {"action": "move", "direction": dir}:
            print(f"Moving {dir}")
        case {"action": "shoot", "target": tgt}:
            print(f"Shooting at {tgt}")


class Status(StrEnum):
    OK = "ok"
    ERROR = "error"


from typing import TypedDict


class Book(TypedDict):
    title: str
    author: str
    year: int


if __name__ == "__main__":
    defaults = {"theme": "dark", "language": "English"}
    custom = {"theme": "light"}
    settings = ChainMap(custom, defaults)
    print(settings["theme"])  # Output: light
    print(settings["language"])  # Output: English

    dd = defaultdict(int)
    # dd["a"] += 1
    print(dd["a"])  # Output: 1

    d = deque([1, 2, 3])
    d.appendleft(0)
    print(d)  # Output: deque([0, 1, 2, 3])
    d.popleft()
    d.pop()
    print(d)  # Output: deque([0, 1, 2, 3])

    counter = Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
    print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
    print(counter["apple"])

    Point = namedtuple("Point", "x y")
    p = Point(10, 20)
    print(p.x, p.y)  # Output: 10 20

    command = {"action": "move", "direction": "north"}
    process_command(command)  # Output: Moving north

    print(Status.OK)

    book1: Book = {"title": "1984", "author": "George Orwell", "year": 1949}
    print(book1)

    large_list = list(range(1, 100000000))
    target = 99999999

    # Binary search on the sorted list
    index = bisect.bisect_left(large_list, target)
    if index < len(large_list) and large_list[index] == target:
        print("Found quickly with binary search!")

    # Simple timing in milliseconds
    start_time = time.time()
    process_large_data()
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Total execution time: {elapsed_time_ms:.2f} ms")

    # Detailed profiling
    cProfile.run("process_large_data()")
