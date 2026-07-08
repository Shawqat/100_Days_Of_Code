# blackJack game
from art import logo
import random

# My solution
# print(logo)
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def check_black_jack(user_cards, computer_cards):
#     total_val_user = sum(user_cards)
#     total_val_pc   = sum(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {total_val_user}")
#     print(f"Computer's final card: {total_val_pc}")

#     if total_val_user > 21 and total_val_pc <= 21:
#         print("User lose")
#     elif total_val_pc > 21 and total_val_user <= 21:
#         print("User win")
#     elif total_val_user > total_val_pc:
#         print("User win")
#     elif total_val_user == total_val_pc:
#         print("Draw!")
#     else:
#         print("User lose")
    
# to_play = "y"
# while to_play == "y":
    
#     user_cards = [random.choice(cards), random.choice(cards)]
#     pc_cards   = [random.choice(cards), random.choice(cards)]

#     print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
#     print(f"Computer's first card: {pc_cards[0]}")

#     to_get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()

#     if to_get_another_card == "y":
#         user_cards.append(random.choice(cards))
#         check_black_jack(user_cards, pc_cards)
#     elif to_get_another_card == "n":
#         check_black_jack(user_cards, pc_cards)
#     else:
#         print("Invalid Choice")

#     print("=" * 40)
#     to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower() 

# Angela Solution

def deal_card():
    "Return  a random card from the deck"
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card  = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, pc_score):
    if u_score == pc_score:
        return "Draw!"
    elif pc_score == 0:
        return "Lose, oponnent has BlackJack"
    elif u_score == 0:
        return "Win with BlackJack"
    elif u_score > 21:
        return "You went over u lose"
    elif pc_score > 21:
        return "Pc went over u win"
    elif u_score > pc_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    user_cards      = []
    computer_cards  = []
    is_game_over    = False
    computer_score  = -1
    user_score      = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over :
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower():
    print("\n" * 50)
    play_game()