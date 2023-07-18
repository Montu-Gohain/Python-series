# ?  Variables and simple data types
from colored import bg

mycolor = bg("blue")
username = "Harry Potter"  # ? Here = is called the assignment operator.
print("Currently the user is : %s" % username)
# If I want to change the value of username to something else.
username = "Montu Gohain"
print("Currently the user is : %s" % username)
num1 = 10
num2 = 3
num3 = 5
result = num1 + num2  # ? Here + is an arithmetic operator addition
result = num1 - num2  # ? Here - is an arithmetia operator subtraction
result = num1 / num2  # ? Here / is divide operator
result = num1 % num2  # ? Here % is modulo operator which returns the remainder

# ? How to store doubles values

result = 3 / 2
rounded_result = 3 // 2
print("Value : ", rounded_result)


# ? Creating a function that takes a message and print that message


def PrintMessage(message):
    print(mycolor, message)


PrintMessage("Hello there, I am learning python, i am a noob but i will learn it.")
