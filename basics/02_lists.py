# A list is a collection of items in a particular order.
# square brackets ([]) indicate a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements
print(bicycles[0])
print(bicycles[0].title())

# -1 in index gives last element of the list
print(bicycles[-1])

bike_message = f"My first bicycle was a {bicycles[0].title()}."
print(bike_message)

# Changing, Adding,Removing , Modifying
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# appending elements at the end of the list
motorcycles.append('Honda')
print(motorcycles)

# inserting elements at any position

motorcycles = ['honda', 'yamaha', 'suzuki']
# insert( index, value )
motorcycles.insert(0, 'supra')

# removing elements
del motorcycles[0]
print(motorcycles)
# removing last element with pop()
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# can remove at any position/index
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove certain element by balue
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.remove('honda')
print(motorcycles)

# print removed element
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")

# Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# sorting PERMANENTLY
cars.sort()
print(cars)

# reverse sorting with reverse=True, use uppercase for True , False
cars.sort(reverse=True)
print(cars)

# sorting TEMPORARILY
sorted(cars)
print(cars)


