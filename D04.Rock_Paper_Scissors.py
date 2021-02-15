import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player1choice = input("Please choose the 1 for rock, 2 for paper, or 3 for scissors?")

player1 = options[int(player1choice) - 1]
player2 = options[random.randint(0, 2)]

def win():
    print("You Win")


def lose():
    print("You lose!")


print("Player 1:\n",player1, "\nPlayer 2:\n", player2)

if player1 == player2:
    print("Draw game!")
elif (player1 == rock and player2 == paper) or (player1 == scissors and player2 == rock) or (player1 == paper and player2 == scissors):
    lose()
else:
    win()
