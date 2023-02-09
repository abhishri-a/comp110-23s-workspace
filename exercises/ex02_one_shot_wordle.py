"""EX02 - one shot wordle"""

__author__ = "730554082"

secret_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

user_guess: str = input("What is your 6-letter guess? ")
letter_index = 0
location_index = 0
result = ""
location: bool = False

while user_guess != secret_word:

    while len[user_guess] != len[secret_word]:
        user_guess: str = input("That was not 6 letters! Try again: ")    
    
    while letter_index < len[secret_word]:
        if secret_word[letter_index] == user_guess[letter_index]:
            result += f"{GREEN_BOX}"
        else:
            while location_index < len[secret_word]:
                if user_guess[letter_index] == secret_word[location_index]:
                    location = True
                    break
                else:
                    location = False
                location += 1
            if location == True:
                result += f"{YELLOW_BOX}"
            else:
                result += f"{WHITE_BOX}"
        letter_index += 1
        location_index = 0
    print(result)
    letter_index = 0
    result = ""
    user_guess: str = input("Not quite. Play again soon! ")

print ("Woo! You got it!")


"""letter_index = 0
j = 0
other: bool = False
user_guess: str = input("What is your 6-letter guess? ")
result = ""


 

while user_guess != secret:
    while len(user_guess)!=6:
    user_guess: str = input("That was not 6 letters! Try again: ")

    while letter_index < 6:
        if secret[letter_index] == user_guess[i]:
            result = f"{result} {GREEN_BOX}"
        else:
           while j < 6:
                if secret[i] == user_guess[j]:
                    other = True
                    break
                else:
                    j+=1
                    other = False
            if other is True:
                result = f"{result} {YELLOW_BOX}"
            else:
                result = f"{result} {WHITE_BOX}"         
        i+=1
        j = 0
    print (result)
    i = 0
    result = ""
    user_guess: str = input("Not quite. Play again soon! ")

print ("Woo! You got it!")"""
