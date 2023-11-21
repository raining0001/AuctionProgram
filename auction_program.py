import art
import random
import name_list

bid_user_information = []

print(art.logo)
print("Welcome to the secret auction game.\n")

def user_input():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    bid_user_information.append({"name": name, "bid": bid})

def computer_bid():
    computer_name = random.choice(name_list.name)
    computer_bid_amount = random.randint(1, 1000)

    bid_user_information.append({"name": computer_name, "bid": computer_bid_amount})

user_bid_number = input("Are there more bidders? Type 'Yes' or 'No'\n")
if user_bid_number.lower() == 'yes':
    user_number = int(input("How many guests?: "))
    for _ in range(user_number):
        computer_bid()
    print("Other guests have made a bid.")
elif user_bid_number.lower() == 'no':
    dictio_empty = len(bid_user_information) == 0
    if dictio_empty:
        print("There aren't any current bets; please place a bet or accept guesses.")
        user_input()
    else:  
        print("The betting will close.")

max_bid = 0
winner = ""
for user_info in bid_user_information:
    if user_info["bid"] > max_bid:
        max_bid = user_info["bid"]
        winner = user_info["name"]

print(f"The winner is {winner} with a bid of {max_bid}.")