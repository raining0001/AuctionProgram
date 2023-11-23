from art import logo
import random
import name_list

bid_user_information = []

def user_bid():
    your_name = input("What is your name?: ")
    your_bid = int(input("What's your bid?: "))

    bid_user_information.append({"name": your_name, "bid": your_bid})

def computer_bid():
    computer_name = random.choice(name_list.name)
    computer_bid_amount = random.randint(1, 1000)

    bid_user_information.append({"name": computer_name, "bid": computer_bid_amount})

def guess_number():
    user_number = int(input("How many guests?: "))
    for num in range(user_number):
       computer_bid()

def guests():
    while len(bid_user_information) == 1:
        if user_bid_number == 'no':
            number_user =int(input("There aren't any current bets from other guests.\n Please chose 1 to make another bet or  2 to have other guesst invited."))
            if number_user == 1:
               user_bid()
            else:
                guess_number()
        else:
            guess_number()

print(logo)                  
print("Welcome to the secret auction game.\n")

user_bid()

user_bid_number = input("Are there more bidders? Type 'Yes' or 'No'\n")

guests()

max_bid = 0
winner = ""
for user_info in bid_user_information:
    if user_info["bid"] > max_bid:
        max_bid = user_info["bid"]
        winner = user_info["name"]

print(f"The winner is {winner} with a bid of {max_bid}.")
