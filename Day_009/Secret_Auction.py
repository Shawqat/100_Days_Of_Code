logo = """
___________
          /
 )_______(
 |"""""""|_.-._,.---------.,_.-._
 |       | | |               | | ''-.
 |       |_| |_             _| |_..-'
 |_______| '-'''---------'' '-'
 )"""""""(
 /_________\
.-------------.
/_______________\
"""

bidders = {}

while True:
    print(logo)
    print("\n", "=" * 40)
    user_name = input("What is your name?: ")
    user_bid  = input("What is your bid?: $")
    bidders[user_name] = user_bid
    
    user_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if user_continue == "no":
        winner_name = max(bidders, key=bidders.get) # to get the key 
        winner_bid = bidders[winner_name] # to get value
        print(f"The winner is {winner_name} with a bid of ${winner_bid}")
        break
    