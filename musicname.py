# import the random module
import random

# print this
print ("""
Welcome to the Music Name Generator
***********************************
""")

# create 2 empty lists
first = []
second = []

# get the CITY, FAVORITE COLOR, and SKIN COLOR of the person
# add the user responses to the first list using .append()
city = input ("Which city did you grow up in? ").title()
first.append(city)
color = input ("What is your favorite color? ").title()
first.append(color)
skin = input ("What is your skin color? ").title()
first.append (skin)

# get the FAVORITE ANIMAL, FAVORITE DRINK, and NICKNAME of the person
# add the user responses to the second list using .append()
animal = input ("What is the name of your favorite animal? ").title()
second.append(animal)
drink = input ("What is your favorite drink? ").title()
second.append(drink)
name = input ("What is your nickname? ").title()
second.append (name)

# assign the boolean TRUE to a variable
# this serves as some sort of switch
cont = True

# create a while loop which will pick random words from both lists
while cont:
    choice1 = random.choice(first)
    choice2 = random.choice(second)

    # and add these words to form a MUSIC NAME
    print (f"Your band name could be {choice1} {choice2}")

    # create an option to either get another name (ie. keep the program running)    
    if input ("Would you like another name? ").lower() == 'yes':
        continue  
    # or end the program by turning the boolean variable to False 
    else:
        cont = False