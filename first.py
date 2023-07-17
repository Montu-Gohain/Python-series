from colored import fg
color = fg('yellow')
myname = "Montu Gohain"
current_year = 2023
lang = "Python"

sentence = "Hello I am %s, in the year %d, I will study %s in depth" % (myname, current_year, lang)
print(sentence)

# ^ Variables

line1 = "************************************************************"
line2 = "*                                                          *"
line3 = "*               Welcome to Python Programming              *"

sequence = [line1, line2, line3, line2, line1]

def PrintWelcome() :
    # ? Looping over the elements of list sequence and printing them one by one

    for line in sequence : 
       print(color + line)

PrintWelcome()
