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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

answer1 = str(input("You come across your first obsticle.\nType left to cut off their head! \nOr type right to give a friendly wave? ")).lower()

option1Correct = "Good job, the carebear had it coming!"
option1Wrong = "You've been ambused by a gang of carebears, ninja elfs from the south pole, and fly. \nThe carebears launched at you and hugged you down so you could not move, \nthe ninja elfs from the south pole, wrapped you up so you could no longer escape, \nand the fly didn't even try to bug you.... \nwhich really bugged you, and caused you to die of loneliness because not even the fly wanted to waste time with you...\nGame Over"

option2Correct = 'Its hot, shirt must come off, you hear a cry for help! You find a life guard board and run after the cry to help as quick as possible... time slows down. \nYour running as fast as you can but almost in slow motion. Sweat slowing going down your body....\n...david hasolhoff.....\nYou noticed you have been running in slow motion for too long and decided to run in regular motion to try and save who ever was crying out for help. \nThey drowned.... well good thing you did not decide to swim.'
option2Wrong = "Due to unfortunate decisions by the board, this game has the same swim physics as GTA Vice City.\nYou cry for help and see someone running over! But while they are running it looks like time is slowing down and they are taking forever... but they look so good. \nYou drown. \nGame Over"

option3Correct = 'You leave the box along and do not touch it. \nYou realize the real treasure was inside you all along and decide to stay on the island... \noh and also you get to keep all the gold that was lying around everywhere on the island as went through it. \nI mean its a treasure island. What else do you think it was made of...'
option3Wrong = 'The box ate you.... \nGame Over'


if answer1 == "left":
  print(option1Correct)
  answer2 = input('After your first fierst battle, you come across a river, \ntype "Swim" to swim across the river, \nOr type "Run" to run along the shore?').lower()
  if answer2 == "run":
    print(option2Correct)
    answer3 = input('You have come to the end of your journey. \nYou come across a box... \nType "Open" to open it or anything else to leave it be?').lower()
    if answer3 == "open":
      print(option3Wrong)
    else:
      print(option3Correct)
  else:
    print(option2Wrong)
else:
  print(option1Wrong)


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
