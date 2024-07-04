# Gussing number game
import random

difficulty = input("Hello in gussing number game :) choose the difficulty of the game :('easy' , 'medium' , 'hard')\n")

if difficulty == "easy":
    remaining_lives = 15
    print("nice you have 15 lives")
elif difficulty== "medium":
    remaining_lives = 10 
    print("nice you have 10 lives")
elif difficulty== "hard":
    remaining_lives = 5
    print("nice you have 5 lives")
    
random_number = random.randint(0,100)

for lives in range(0,20) :
    user_guess = int(input("Guess a number between 0 to 100 !\n"))
    if user_guess > random_number :
     print("TOO HIGTH!")
     remaining_lives -= 1
     print(f"you have {remaining_lives} remaining lives")
    elif user_guess < random_number :
        print("TOO LOW!")
        remaining_lives -= 1
        print(f"you have {remaining_lives} remaining lives")
    else:
        print(f"That's right the actual number is {random_number} you won")
        break
    if remaining_lives == 0 :
        print("You ran out of lives game over!!")
        break
