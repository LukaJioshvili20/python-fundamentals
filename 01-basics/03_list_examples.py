# Looping Through an Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("Name:", magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

for value in range(1, 5):
    print(value)

# creating list of numbers
numbers_list = list(range(1, 11))
print(numbers_list)

# Skipping indexes
numbers_even_list = list(range(2, 11, 2))
print(numbers_even_list)

# adding square of numbers
numbers_squared = []
for value in range(1, 11):
    square = value ** 2
    numbers_squared.append(square)

print(numbers_squared)

# min,max,sum
print(min(numbers_squared))
print(max(numbers_squared))
print(sum(numbers_squared))

# List Comprehensions, oneliner
numbers_squared_short = [value ** 2 for value in range(1, 11)]
print(numbers_squared_short)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:])
print(players[:4])

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append("Pizza")

# Tuples - immutable list is called a tuple.
dimensions = (64, 64)
print("Old Tuple", dimensions[0], dimensions[1])

# dimensions[0] = 128 can not mutate tuple values
# but we can overwrite
dimensions = (128, 128)
print("New Tuple", dimensions[0], dimensions[1])

