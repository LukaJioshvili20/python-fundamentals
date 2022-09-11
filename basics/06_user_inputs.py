# input() function pauses program
# waits for the user to enter some text

# input_message = input("Tell me something :")
# print(input_message)

#
# input_name = input("Enter your name:")
# print(f"\nHello, {input_name}!")

# input_prompt = "If you tell us who you are, we can personalize the messages you see."
#
# input_prompt += "\nWhat is your first name?"
#
# input_name = input(input_prompt)


# Using int() to Accept Numerical Input

# input_age = input("How old are you ?")
# print(int(input_age) >= 18)

# The Modulo Operator

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# Letting the User Choose When to Quit

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# active = True

# EXIT WAY 1
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# EXIT WAY 2
# while active:
#     message = input(prompt)
#
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# EXIT WAY 3

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(prompt)
#     if city == "quit":
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# Moving Items from One List to Another

# start with users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ["walter", 'crazy8', 'jessy', 'hank']
confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# remove all cats from the list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input

user_responses = {}
is_active = True

while is_active:
    name = input("\nWhat is your name? ")
    response = input("which mountain would you like to climb someday? ")

    user_responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        is_active = False

print("\n--- Poll Results ---")
for name , response in user_responses.items():
    print(f"{name} would like to climb {response}.")
