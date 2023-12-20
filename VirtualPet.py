# imports
import time
import threading
import os
import random

"""
Class to represent a virtual pet.

int food: The current level of satiation of the virtualPet. the higher the food value, the less hungry tha virtualPet is

int maxFood: The maximum level of satiation the virtualPet can reach.

int avatar: the virtualPet will have an avatar made using ascii art, the initial character, a cat, will be defined as 0
"""
class virtualPet:

    eyes = "   /  o   o  \\"
    eyeBlink = "   /  _   _  \\"
    middle = "   )         (\n  (           )"



    """
    Constructor to instantiate the virtualPet class.
    
    params: 
    maxFood: int, optional (default: 100)
        The maximum level of food the virtualPet can reach.
    avatar: int (default: 0 for a cat)
        The pictorial representation of your pet
    name: string
        its name lol
    
    """
    def __init__(self, name, maxFood: int = 100, avatar: int = 0):
        ##initializing our pets fields to either passed in values, or defaults
        self.food = 100  # Initializing the food level to 100 (pet is not hungry at first)
        self.maxFood = maxFood  # Setting the maximum food level
        self.avatar = avatar
        self.name = name

        


        self.foodThread = threading.Thread(target=self.reduceFood)
        self.foodThread.daemon = True  # Mark as a daemon thread cause its just in the background
        self.foodThread.start()

        
        self.blinkThread = threading.Thread(target=self.blink)
        self.blinkThread.daemon = True
        self.blinkThread.start()


    """
    Updates the food level of the virtualPet by subtracting 1 every 5 minutes
    """
    def reduceFood(self):
        while self.food > 0:
            time.sleep(3)  # Wait for 5 minutes
            with threading.Lock():
                self.food -= 1

                ##just for testing, remove when done so decrementation is behind the scenes
                #print(f"{self.name}'s food level is now: {self.food}") 

    """
    Feeds the virtualPet by increaasing its food level by 10.
    returns A message indicating that the virtualPet has been fed.
    """
    def feed(self):
        with threading.Lock():
            if self.food < self.maxFood:
                if self.food > 90:
                    self.food = 100
                else:
                    self.food += 10
                print(f"{self.name} has been fed. Food level is now: {self.food}")

    """
    Prints out the virtualPet and makes it blink at pseudorandom intervals
    """
    def blink(self):
            while True:
                time.sleep(random.randrange(7, 15, 1))  # blink every 7-15 seconds
                os.system('cls||clear')
                print("    /\\_____/\\")
                print(self.eyes)
                print("  ( ==  ^  == )")
                print(self.middle)
                print(" (             )")
                print("(__(,,)___(,,)__)")
                time.sleep(0.2)
                os.system('cls||clear')
                print("    /\\_____/\\")
                print(self.eyeBlink)
                print("  ( ==  ^  == ) ")
                print(self.middle)
                print(" (             )")
                print("(__(,,)___(,,)__) ")
                time.sleep(0.2)
                os.system('cls||clear')
                print("    /\\_____/\\")
                print(self.eyes)
                print("  ( ==  ^  == )")
                print(self.middle)
                print(" (             )")
                print("(__(,,)___(,,)__)")
                time.sleep(0.3)
                os.system('cls||clear')
                print("    /\\_____/\\")
                print(self.eyeBlink)
                print("  ( ==  ^  == ) ")
                print(self.middle)
                print(" (             )")
                print("(__(,,)___(,,)__) ")
                time.sleep(0.2)
                os.system('cls||clear')
                print("    /\\_____/\\")
                print(self.eyes)
                print("  ( ==  ^  == )")
                print(self.middle)
                print(" (             )")
                print("(__(,,)___(,,)__)")
                print(f"Type 'feed' to feed {self.name}, or 'dress' to give {self.name} an outfit!")
    
    """
    allows the virtual pet to be dressed
    """
    def dress(self, outfit):
        while True:
            if outfit == 'tie':
                self.middle = "   )    ◆    (\n  (     ♢     )"
                break
            elif outfit == 'default':
                self.middle = "   )         (\n  (           )"
                self.blink = "   /  _   _  \\"
                self.eyes = "   /  o   o  \\"
                break
            elif outfit == 'bowtie':
                self.middle = "   )   ▷◆◁   (\n  (           )"
                break
            elif outfit == 'glasses':
                self.eyes = "   /--⬡---⬢--\\"
                break
            else:
                print("Invalid input! Please enter 'tie', 'bowtie', 'glasses' or 'default'!")






#Running the virtualPet class:

# Creating a pet using all default values
print("Enter your pets name!")
petName = input()

myPet = virtualPet(petName)
running = True

while running:

    command = input()

    if command.lower() == 'feed':
        myPet.feed()

    if command.lower() == 'dress':
        print("Enter 'bowtie' to dress your pet in a bowtie, 'tie' to dress your pet in a tie,")
        print("'glasses' to give your pet some shades, or 'default' to reset your pets outfit ")
        outfit = input()
        myPet.dress(outfit.lower())