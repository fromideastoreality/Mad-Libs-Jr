import wikipedia
import time


print("----------------------------------")
print("|WELCOME TO MAD LIBS JR. Ver. 1.0|")
print("----------------------------------")
#Displays a welcome Banner for the game to the console.
time.sleep(2) #Using the time function gives the user a chance to read content printed to the console.
#To expand upon this game, prompt the user to create their own username for the game. 
#There should be defined rules on the requirements for username creation.
print("Hello there and thanks for playing! Are you new to the game?")
#Prints a string that finds out if the user is familiar with Mad Libs. If they are not, the game calls on the Wikipedia API to provide a brief summary.
answer = None
while answer not in ("Y", "N"):
    answer = input("Enter Y for yes, or N for no: ")
    if answer == "Y":
        print("No worries. Here is a brief introduction to get you started:\n")
        print(wikipedia.summary("Mad Libs"))
    elif answer == "N":
        print("Awesome! Let's dive right in.")
    else:
        print("Please enter Y for yes, or N for no: ") #This can be improved to continuously prompt the user for the correct input. 
time.sleep(5)
print("\n")
time.sleep(2)
print("Let's begin shall we?\n")
#Below are the rules for the game. 
color = input ("What's your favorite color?: ")
plural_noun = input ("Enter a plural noun: ")
celebrity = input ("Who's your favorite celebrity?: ")
potus = input ("Name one U.S. president: ")
print("\n")

#we have created 3 variables, in which the user's input will be stored. 

print("Yo dog! I heard that:\n")
print("Roses are " + color)
print(plural_noun + " are blue")
print("You love " + celebrity)
print("And so does " + potus)
time.sleep(3)
print("P.S....." + " Don't tell " + potus + " that I told you his secret!")
#At this point, the game is basically finished. Adapt the game to prompt the user to continue playing (e.g. using a loop/condition). If the user says no, break the loop and end the program.
time.sleep(3)
print("Thanks for playing! The game will close on its own shortly. ")
time.sleep(7)
