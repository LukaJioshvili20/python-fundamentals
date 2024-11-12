from random import sample

d = {"a": [], "b": [], "c": [], "d": []}

for key, val in d.items():
    if key == "a":
        val.extend(sample(range(0, 100), 3))
    elif key == "b":
        val.extend(sample(range(0, 100), 4))
    elif key == "c":
        val.extend([0, 0, 0, 0])
    elif key == "d":
        val.extend(sample(range(0, 100), 9))

print(d)


def get_data(input_dict):
    largest_key = None
    value_mult = 1

    for key, value in input_dict.items():
        if largest_key is None or len(value) > len(input_dict[largest_key]):
            largest_key = key

        for n in value:
            value_mult *= n

    return largest_key, value_mult


print(get_data(d))
