import random
from data import info, logo, vs


def select_two_characters(data):
    """Return two different random characters."""
    return random.sample(list(data.items()), 2)


def display_characters(a, b):
    print(logo)
    print(
        f"Compare A: {a[0]}, "
        f"{a[1]['description']}, "
        f"{a[1]['country']}"
    )
    print(vs)
    print(
        f"Against B: {b[0]}, "
        f"{b[1]['description']}, "
        f"{b[1]['country']}"
    )


def get_winner(a, b):
    """Return 'A' if A has more followers, otherwise 'B'."""
    if a[1]["followers"] >= b[1]["followers"]:
        return "A"
    return "B"


def game_play():
    score = 0
    character_a, character_b = select_two_characters(info)

    while True:
        display_characters(character_a, character_b)
        print(f"Current score: {score}\n")
        guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if guess not in ("A", "B"):
            print("Invalid choice.\n")
            continue

        winner = get_winner(character_a, character_b)

        if guess == winner:
            score += 1
            print("\nYou're right!\b")

            # Winner stays, loser is replaced
            if winner == "A":
                character_b = random.choice(list(info.items()))
                while character_b == character_a:
                    character_b = random.choice(list(info.items()))
            else:
                character_a = character_b
                character_b = random.choice(list(info.items()))
                while character_b == character_a:
                    character_b = random.choice(list(info.items()))
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            break


game_play()