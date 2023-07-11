# Computer asks us
# What is your name?
# What is your age?
# What is your country?

# We give a response
# We expect a feedback like:

# Welcome name, i see you are from country, but you are age years old.

pickName = input("what is your name\n")
pickAge = input("what is your age\n")
pickCountry= input("what is your country\n")

print(f"Welcome {pickName},i see you are from {pickCountry}, but you are {pickAge} years old")

# Explanation
# The code begins by using the input() function to prompt the user with the question "What is your name?".
#  The user's input is then stored in the pickName variable.
# Similarly, the code uses the input() function again to prompt the user with the question "What is your age?".
# The user's input is stored in the pickAge variable.
# Next, another input() function is used to prompt the user with the question "What is your country?".
#  The user's input is stored in the pickCountry variable.
# The f-string allows us to embed the variables name, country, and age directly into the string.
# The curly braces {} are used to enclose the variables, and they will be replaced with the respective values when the string is formatted.
# Finally, the code uses the print() function to display the feedback string, which includes the personalized message based on the user's inputs.