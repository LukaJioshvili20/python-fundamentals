# common_string_methods.py

"""
This module demonstrates common string methods in Python with examples.
"""


def capitalize_example():
    """
    Capitalizes the first letter of a string.
    """
    return "hello".capitalize()  # Output: 'Hello'


def casefold_example():
    """
    Converts the string to lowercase, with more aggressive lowercasing for certain characters.
    """
    return "Hello".casefold()  # Output: 'hello'


def center_example():
    """
    Centers the string with a given width and pads it with the specified character.
    """
    return "hello".center(10, "*")  # Output: '***hello**'


def count_example():
    """
    Counts the occurrences of a substring in the string.
    """
    return "hello world".count("o")  # Output: 2


def endswith_example():
    """
    Checks if the string ends with a specific suffix.
    """
    return "hello".endswith("lo")  # Output: True


def find_example():
    """
    Finds the index of the first occurrence of a substring, or returns -1 if not found.
    """
    return "hello".find("e")  # Output: 1


def format_example():
    """
    Formats the string using placeholders.
    """
    return "My name is {}".format("John")  # Output: 'My name is John'


def index_example():
    """
    Finds the index of a substring and raises ValueError if not found.
    """
    return "hello".index("e")  # Output: 1


def isalnum_example():
    """
    Checks if all characters in the string are alphanumeric.
    """
    return "hello123".isalnum()  # Output: True


def isalpha_example():
    """
    Checks if all characters in the string are alphabetic.
    """
    return "hello".isalpha()  # Output: True


def isdigit_example():
    """
    Checks if all characters in the string are digits.
    """
    return "123".isdigit()  # Output: True


def islower_example():
    """
    Checks if all characters in the string are lowercase.
    """
    return "hello".islower()  # Output: True


def isupper_example():
    """
    Checks if all characters in the string are uppercase.
    """
    return "HELLO".isupper()  # Output: True


def isspace_example():
    """
    Checks if the string contains only whitespace characters.
    """
    return "   ".isspace()  # Output: True


def join_example():
    """
    Joins an iterable with the string as a separator.
    """
    return "-".join(["a", "b", "c"])  # Output: 'a-b-c'


def lstrip_example():
    """
    Removes leading characters (whitespace by default).
    """
    return "   hello".lstrip()  # Output: 'hello'


def rstrip_example():
    """
    Removes trailing characters (whitespace by default).
    """
    return "hello   ".rstrip()  # Output: 'hello'


def strip_example():
    """
    Removes both leading and trailing characters (whitespace by default).
    """
    return "   hello   ".strip()  # Output: 'hello'


def lower_example():
    """
    Converts all characters to lowercase.
    """
    return "HELLO".lower()  # Output: 'hello'


def upper_example():
    """
    Converts all characters to uppercase.
    """
    return "hello".upper()  # Output: 'HELLO'


def partition_example():
    """
    Splits the string into a tuple of three parts: before the separator, the separator itself, and after.
    """
    return "hello world".partition(" ")  # Output: ('hello', ' ', 'world')


def replace_example():
    """
    Replaces occurrences of a substring with another substring.
    """
    return "hello world".replace("world", "Python")  # Output: 'hello Python'


def split_example():
    """
    Splits the string into a list of substrings.
    """
    return "a,b,c".split(",")  # Output: ['a', 'b', 'c']


def splitlines_example():
    """
    Splits the string into a list of lines.
    """
    return "line1\nline2".splitlines()  # Output: ['line1', 'line2']


def startswith_example():
    """
    Checks if the string starts with a specific prefix.
    """
    return "hello".startswith("he")  # Output: True


def swapcase_example():
    """
    Swaps the case of all characters in the string.
    """
    return "Hello".swapcase()  # Output: 'hELLO'


def title_example():
    """
    Converts the first letter of each word to uppercase.
    """
    return "hello world".title()  # Output: 'Hello World'


def zfill_example():
    """
    Pads the string with zeros to the left, to match the specified width.
    """
    return "42".zfill(5)  # Output: '00042'


def slice_full_string():
    """
    Returns the full string using default step (1).
    """
    return "hello world"[::1]  # Output: 'hello world'


def reverse_string():
    """
    Reverses the string using step (-1).
    """
    return "hello world"[::-1]  # Output: 'dlrow olleh'


def slice_from_start_to_index():
    """
    Slices the string from index 0 to index 4.
    """
    return "hello world"[0:5]  # Output: 'hello'


def slice_from_index_to_end():
    """
    Slices the string from index 6 to the end.
    """
    return "hello world"[6:]  # Output: 'world'


def slice_from_start_to_index_5():
    """
    Slices the string from the start to index 4.
    """
    return "hello world"[:5]  # Output: 'hello'


def every_second_character():
    """
    Extracts every second character from the string.
    """
    return "hello world"[::2]  # Output: 'hlowrd'


def every_second_character_from_index_1():
    """
    Extracts every second character starting from index 1.
    """
    return "hello world"[1::2]  # Output: 'el ol'


def every_second_character_reverse():
    """
    Extracts every second character in reverse order.
    """
    return "hello world"[::-2]  # Output: 'drwolh'


def slice_from_index_3_to_7():
    """
    Slices the string from index 3 to index 7.
    """
    return "hello world"[3:8]  # Output: 'lo wo'


def slice_with_step_from_index_3_to_7():
    """
    Slices the string from index 3 to index 7 with a step of 2.
    """
    return "hello world"[3:8:2]  # Output: 'l o'


def reverse_slice_from_index_8_to_4():
    """
    Slices the string in reverse order from index 8 to 4.
    """
    return "hello world"[8:3:-1]  # Output: 'o w'


def slice_last_5_characters():
    """
    Slices and returns the last 5 characters of the string.
    """
    return "hello world"[-5:]  # Output: 'world'


def slice_except_last_5_characters():
    """
    Slices and returns the string excluding the last 5 characters.
    """
    return "hello world"[:-5]  # Output: 'hello '


def reverse_every_second_character_from_last():
    """
    Reverses the string and extracts every second character starting from the last character.
    """
    return "hello world"[-1::-2]  # Output: 'drwolh'


if __name__ == "__main__":
    # Running each function to see the outputs.
    print("capitalize_example:", capitalize_example())
    print("casefold_example:", casefold_example())
    print("center_example:", center_example())
    print("count_example:", count_example())
    print("endswith_example:", endswith_example())
    print("find_example:", find_example())
    print("format_example:", format_example())
    print("index_example:", index_example())
    print("isalnum_example:", isalnum_example())
    print("isalpha_example:", isalpha_example())
    print("isdigit_example:", isdigit_example())
    print("islower_example:", islower_example())
    print("isupper_example:", isupper_example())
    print("isspace_example:", isspace_example())
    print("join_example:", join_example())
    print("lstrip_example:", lstrip_example())
    print("rstrip_example:", rstrip_example())
    print("strip_example:", strip_example())
    print("lower_example:", lower_example())
    print("upper_example:", upper_example())
    print("partition_example:", partition_example())
    print("replace_example:", replace_example())
    print("split_example:", split_example())
    print("splitlines_example:", splitlines_example())
    print("startswith_example:", startswith_example())
    print("swapcase_example:", swapcase_example())
    print("title_example:", title_example())
    print("zfill_example:", zfill_example())
    # String slicing and methods
    print("Full string:", slice_full_string())
    print("Reversed string:", reverse_string())
    print("Slice from start to index 4:", slice_from_start_to_index())
    print("Slice from index 6 to end:", slice_from_index_to_end())
    print("Slice from start to index 5:", slice_from_start_to_index_5())
    print("Every second character:", every_second_character())
    print("Every second character from index 1:", every_second_character_from_index_1())
    print("Every second character in reverse:", every_second_character_reverse())
    print("Slice from index 3 to 7:", slice_from_index_3_to_7())
    print("Slice with step from index 3 to 7:", slice_with_step_from_index_3_to_7())
    print("Reverse slice from index 8 to 4:", reverse_slice_from_index_8_to_4())
    print("Last 5 characters:", slice_last_5_characters())
    print("Slice except last 5 characters:", slice_except_last_5_characters())
    print(
        "Reverse every second character from last:",
        reverse_every_second_character_from_last(),
    )
