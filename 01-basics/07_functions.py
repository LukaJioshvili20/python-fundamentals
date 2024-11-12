def greet_user(username='Guest'):
    print(f"Hello there ! {username}")


greet_user('Luka')


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# can call multiple times ( order matter ! )
describe_pet('doggo', 'larry')
describe_pet('doggo', 'jerry')

# can give keyword arguments ( order does not matter now )
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#

# kimi = get_formatted_name('kimi', 'raikkonen')
# print(kimi)


# Making an Argument Optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if (middle_name):
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name
#
#
# teacher = get_formatted_name('walter', 'white')
# print(teacher.title())
#
# teacher = get_formatted_name('walter', 'white', 'hartwell')
# print(teacher.title())

# Returning a Dictionary
#
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
#
# musician = build_person('jimi', 'hendrix')
# print(musician)

#
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'quit' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'quit':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'quit':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# Arbitrary number of arguments
# def make_lobiani(*toppings):
#     print("\nMaking a lobiani with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_lobiani('lobio')
# make_lobiani('lobio', 'lori', 'sunelebi')

# Mixing Positional and Arbitrary Arguments
def make_lobiani(size, *toppings):
    print(f"\nMaking a {size}-inch lobiani with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_lobiani(18, 'lobio')
make_lobiani(12, 'lobio', 'lori', 'sunelebi')


# when you do not know what will come inside the function

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('luka', 'jioshvili', location='Tbilisi', field='web development')
print(user_profile)

# import whole file to another
# can use alias es using "as" keyword to module
# import modules.make_pizza as pizza
# pizza.make_pizza(16, 'pepperoni')

# Specific function
# from modules.make_pizza import make_pizza
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from modules.make_pizza import and give alias to imported function
# from modules.make_pizza import make_pizza as pizza_maker_function
# pizza_maker_function(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing everything from module
from modules.make_pizza import *
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
