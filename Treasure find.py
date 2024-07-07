print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Enchanted Forest.")
print("Your mission is to find the hidden treasure.")

choice1 = input('You are standing at the edge of an enchanted forest. Do you want to enter the forest or stay outside? Type "enter" or "stay" \n').lower()
if choice1 == "enter":
    choice2 = input('You\'ve entered the forest and come across a magical creature who offers you a choice. Type "help" to ask for help or "ignore" to ignore the creature. \n').lower()
    if choice2 == "help":
        choice3 = input("The creature offers you two paths: one through the dark woods and one through the sunny glade. Which path do you choose? Type \"dark\" or \"sunny\" \n").lower()
        if choice3 == "dark":
            print("You get lost in the dark woods and encounter a pack of wolves. Game Over.")
        elif choice3 == "sunny":
            choice4 = input("You walk through the sunny glade and find a hidden cave. Do you want to enter the cave? Type \"yes\" or \"no\" \n").lower()
            if choice4 == "yes":
                print("You enter the cave and find the hidden treasure! You Win!")
            else:
                print("You decide not to enter the cave and miss out on the treasure. Game Over.")
        else:
            print("You chose a path that doesn't exist. Game Over.")
    else:
        print("You ignore the creature and wander aimlessly until you get hopelessly lost. Game Over.")
else:
    print("You decide to stay outside and miss out on the adventure. Game Over.")


