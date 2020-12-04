print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input(
    'Your\'e at a fork in the road... which path do you take? Type "left" or"right" \n'
).lower()
if choice1 == "left":
    choice2 = input(
        'You stumble upon a river. On the other side you can see a castle! Type "walk" to walk upstream in search of a bridge. Type "swim" to swim accross. \n'
    ).lower()
    if choice2 == "walk":
        choice3 = input(
            'You made it accross safely! Upon reaching the castle you see it has three doors, one red, one yellow, one blue. Which do you choose? \n'
        ).lower()
        if choice3 == "blue":
            print(
                "You fling open the door, surprised and elated at your apparent success only to trip and fall into A PIT OF DRAGONS! 😩 "
            )
        elif choice3 == "red":
            print(
                "As you open the door and see the treasure gleaming in the sunlight streaming in from behind you... in the distance you hear a beeping... your eyelids begin to flutter as you reach for the nearest gold coin.. waaaait a minute! This was all a dream... and to top it off you are going to be late to work! "
            )
        elif choice3 == "yellow":
            print(
                "The heavy wooden door CREEEAAAAAKS slooooowly open, as you step inside you see what you have been searching for all this time! CONGRATS! You have found the grail... A magic phone battery that NEVER runs out of charge!! 🥳"
            )
        else:
            print("You chose a door that does not exist. GAME OVER")
    else:
        print(
            "AAAAH ITS A LAKE FULL OF DEADLY GIANT LEECHES!!!!!! needless to say... no treasure for you...😳"
        )
else:
    print(
        "OH NO! you walked right into the path of a hungry bear... no treasure today (or anyday... for that matter...😭 )"
    )