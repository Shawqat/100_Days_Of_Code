import string

chars = string.ascii_lowercase
logo = """


        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88        
"""

def caesar_cipher(message, operation):
    converted_messge = ""
    for letter in message:
        if letter not in chars:
            converted_messge += letter
        else:
            if operation == "encode":
                letter_index = chars.index(letter) + shift
            elif operation == "decode":
                letter_index = chars.index(letter) - shift

            letter_index %= len(chars)
            converted_messge += chars[letter_index]

    return f"your {operation}ed message {converted_messge}"

should_continue = True 

while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text      = input("Type your message: \n").lower()
    shift     = int(input("Type the shift number: \n"))

    print(caesar_cipher(text,direction))
    user_choice = input("do you want to continue ?: (y or n) ").lower()
    if user_choice == "y":
        should_continue = should_continue
        print("=" * 40)
    else:
        should_continue = False
        print("Thank to us our app :D")
