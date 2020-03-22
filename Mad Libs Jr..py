import wikipedia
import time

print("----------------------------------")
print("|WELCOME TO MAD LIBS JR. Ver. 1.0|")
print("----------------------------------")
#Displays a welcome Banner for the game to the console.
time.sleep(5) #Using the time function gives the user a chance to read content printed to the console.
#To expand upon this game, prompt the user to create their own username for the game. 
#There should be defined rules on the requirements for username creation.
print("Hello there and thanks for playing! Are you new to Mad libs?")
#Prints a string that finds out if the user is familiar with Mad Libs. If they are not, the game calls on the Wikipedia API to provide a brief summary.
answer = input("Enter Y for yes, or N for no: ")
if answer == "Y":
    print("Here is a summary from good 'ole Wikipedia: \n")
    print(wikipedia.summary("Mad Libs"))
elif answer == "N":
    print("Awesome! Let's dive right in.")
else:
    print("Please enter Y for yes, or N for no: ") #This can be improved to continuously prompt the user for the correct input. 
time.sleep(5)
print("\n")


#Below are the rules for the game. 
print("Roses are {color}")
print("{plural} are blue")
print("I love {celebrity}")
time.sleep(5)
