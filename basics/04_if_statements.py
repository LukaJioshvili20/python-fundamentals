cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#  Checking for Equality
car = "Audi"
print(car == "bmw")
# Ignoring Case When Checking for Equality
car = "Audi"
print(car.lower() == 'audi')
# Checking for Inequality

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
else:
    print("anchovies !")

# for Checking Multiple Conditions use: and , or

# check if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print('garlic' not in requested_toppings)

# Boolean Expressions
game_active = True
can_edit = False

age = 2
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


# multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
else:
    print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
