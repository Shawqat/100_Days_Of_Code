import random
words_list = ["camel","baboon","dog"]

secret_word = random.choice(words_list)
lives = 6

print("""
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/
""")

secret_status = len(secret_word) * "_"
print(f"Word to guess: ", secret_status)

correct_letters = []
game_over = False

while not game_over:
    guess = input("guess a letter: ").lower()
    display = ""
    
    for letter in secret_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
           
        elif letter in correct_letters:
            display += letter
            
        else:
            display += "_"
            

    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
            
    print(display)
    print("=" * 20, f"You have {lives} left.", "=" * 20)

    if "_" not in display:
        game_over = True
        print("You won")

    



