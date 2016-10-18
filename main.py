import random
import time
import insult_list

print("Welcome to the Insult-o-Matic")

def getName():
    name = input("Please enter your name: ")
    if name:
        #Always capitalise first letter
        return name.replace(name[0], name[0].upper(), 1)
    else:
        print("I'm sorry, how do you spell that again?")
        #Ask for the name again recusively. return the answer all the way back to the top
        return getName()

def insult(name):
    size      = random.choice( insult_list.size() )
    adjective = random.choice( insult_list.adjective() )
    noun      = random.choice( insult_list.noun() )

    print( "\n{0} you are a {1} {2} {3}!\n".format(name, size, adjective, noun) )

    time.sleep(2)

while True:
    answer = input("Do you want me to insult you? Yes or No: ")
    if answer and answer[0].lower() == "y":
        insult( getName() )
    else:
        print("OK, I'll get you next time.")
        quit()
