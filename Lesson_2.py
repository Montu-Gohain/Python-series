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
