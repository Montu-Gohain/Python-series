"""
^ Let's Learn how to use String efficiently in Python
"""
from colored import bg

bluebg = bg("blue")

prime_minster = "Modiji"
print("Our Current Prime Minister is : %s" % (prime_minster))


# ? Let's covert any string to title case
def ConverToTitle(str):
    print("Your Output is  : ", str.title())


input = "JAMES BOND"
ConverToTitle(input)


# ? Let's convert any string to lower case using .lower() method
def ConverToLower(str):
    print("Your output is : %s" % str.lower())


ConverToLower(input)


# ? Convert any string to uppercase using .upper() method
def ConvertToUpper(str):
    print(bluebg, "Using upper method : %s" % str.upper())


input = "the assam tribune"
ConvertToUpper(input)

# ? Adding whitespaces with a tab or newline

print("I Know these languages : \n\tJavascript\n\tJython\n\tC++\n\tSQL")
# Here \n will print in a new line and \t will give a tab

# ? How to do string concatination in pythong , simple old way just add them

first_name = "Albert"
last_name = " Einstein"
print("Theory of relativity was created by : ", first_name + last_name)

# ? How to strip white spaces using strip() method

word_w_spaces = " AWOSOME "
rightStriped = word_w_spaces.rstrip()
print(rightStriped)

leftStriped = word_w_spaces.lstrip()
print(leftStriped)

bothStriped = word_w_spaces.strip()
print(bothStriped)

# ? How to remove whitespace in between two strings

sentence = "Hello There"
sentence_ = sentence.replace(" ", "")
print(sentence_)

# ^ Rule for using apostrophes in strings (Its better to use double quotes instead of single quotes)
opinion = "One of the python's strengths is its diversity"
