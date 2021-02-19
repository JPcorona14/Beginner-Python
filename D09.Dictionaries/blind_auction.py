from replit import clear
from art import *


print(logo)

bids = []
add_more = True
Winner = ""
Highest_Bid = 0

def new_bid(user, amount):
    players = {}
    players["name"] = user
    players["dollar"] = amount

    bids.append(players)


while add_more:
    new_player = input("Please Enter your name?\n")
    bid_amount = int(input("Please enter your bid?\n$"))
    continue_game = input("Will there be another person bidding: Y for Yes / N for No\n").lower()

    new_bid(user = new_player, amount= bid_amount)

    if continue_game == "n":
        add_more = False

    clear()

for x in bids:
    current_name = ""
    current_amount = 0
    for y in x:
        if y == "name":
            current_name = x[y]
        elif y == "dollar":
            current_amount = x[y]
    
    if current_amount > Highest_Bid:
        Winner = current_name
        Highest_Bid = current_amount

print(f"The winner is {Winner} with the bid amount of ${Highest_Bid}!")

