my_list = [169, 254, 56, 103]


# map - changes the value of input with a function inside iterable
def power_up(number: int) -> int:
    return number + 123


# print(list(map(power_up, my_list)))
# filter -filters out values from a condition
def odd_numbers(number: int) -> int:
    if number % 2 == 0:
        return True
    return False


print(list(filter(odd_numbers, my_list)))
