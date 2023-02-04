import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
        top_of_range=int(top_of_range)
    
if top_of_range <= 0:
        print("Please enter number larger than 0")
        
else:
    print("Please enter a number!")
    quit()
    
    
random_number=random.randint(0,top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
         user_guess = int(user_guess)
    else:
        print("Please enter a number!")
        continue
    

    if user_guess == random_number:
        print("You win!")
        break
    elif user_guess > random_number:
             print("Above the number")
    else:
            print("You below number")
            
print("You got", guesses, "guesses")


