print("Zǎo ān, zhōngguó")

# Variables
message = "Zǎo ān, zhōngguó"
print(message)
message = "hello there"
print(message)

# Naming

# Variable names should start with a letter or an underscore
greeting_message = "Howdy"
print(greeting_message)

_salut = "Howdy sir"
print("_salut : ", _salut)

s_n = "Luka"  # Bad
student_name = "luka"  # Good
student_surname = "jioshvili"
# Strings
single_quotes = "This is a string."
double_quotes = 'This is also a string.'

combined_string = 'I told my friend, "Python is my favorite language!"'
combined_string_vise = "The language 'Python' is named after Monty Python, not the snake."
print(combined_string)
print(combined_string_vise)

# String methods
print(student_name.title())  # luka => Luka
print(student_name.upper())  # luka => Luka
print(student_name.lower())  # LUKA => luka

# Variables inside String
# Put f before string to insert variable values
# F stands for f-strings f = "format" python => v3.6
student_full_name = f"Hello Mr. {student_name} {student_surname}"
print(student_full_name.title())

# spaces in Strings
print("Python")
# \t adding whitespace in string
print("\tPython")
# \n for new line
print("Languages:\nPython\nC\nJavaScript")
# \n \t combo
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping/removing whitespace
favorite_language = "Mandarin "
print(favorite_language, len(favorite_language))
print(favorite_language.rstrip(), len(favorite_language.rstrip()))
# rstrip() to right , lstrip() to left

# Numbers

# add (+), subtract (-), multiply (*), and divide (/)
# times **
number_times = 3 ** 2
print("3 times 2 eqauals", number_times)

# can add underscores in numbers
your_dads_age = 14_000_000_000
print(your_dads_age)

# can to multiple Assignments
x, y, z = 1, 2, 3
print(x, y, z)

# python does not have built-in constants
# but we write constants with uppercase letters only
MAX_SUBNETS = 40

# import this
