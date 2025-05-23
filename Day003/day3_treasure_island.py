def print_treasure_ascii():
    treasure_art = r'''
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
/______/______/______/______/______/______/______/______/______/______/[Mulinga]
*******************************************************************************
'''
    print(treasure_art)

print_treasure_ascii()

print("*******************************************************************************")
print("Welcome to Treasure Island!!!!!!!!\nYour Mission is to find the treasure 💰")
print("*******************************************************************************")

choice1 = input("You're at a cross-road. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n"
        "Type 'wait' to wait for a boat or type 'swim' to swim across: ").lower()

    if choice2 == "wait":
        print("⛵ A mysterious boat arrives and takes you safely across the lake...")
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue.\n"
            "Which door do you choose? Type 'red', 'yellow', or 'blue': ").lower()

        if choice3 == "red":
            print("🔥 The room is full of fire. You got burnt! Game Over. ☠️")
        elif choice3 == "blue":
            print("🐊 The room is full of crocodiles. You were eaten alive! Game Over. ☠️")
        elif choice3 == "yellow":
            print("🎉 You found the treasure! Congratulations, adventurer! 🏆")
            print("        🪙💰🏝️ THE END 💰🪙")
        else:
            print("You chose a door that doesn't exist. You vanish into the abyss... Game Over. ☠️")

    elif choice2 == "swim":
        print("🦈 You were attacked by angry trout and dragged underwater. Game Over. ☠️")
    else:
        print("That wasn't an option. A ghost ship appears and takes you away forever... Game Over. 👻")

elif choice1 == "right":
    print("😈 Oh no! You fell into a trap set by pirates and were captured!")
    print("They force you to walk the plank... SPLASH! Game Over. ☠️")

else:
    print("You stood still for too long... A thunderstorm hits and lightning strikes! ⚡ Game Over. ☠️")







