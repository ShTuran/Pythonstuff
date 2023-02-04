import random

user_wins = 0
computer_wins =0

choice =  ["rock","paper","scissors"] 

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q" :
        break
    
    if user_input not in choice:
        print("Please select from given items")
        continue
    
    random_number = random.randint(0,2)
    #   rock 0, scissor 1, paper 2
    computer_pick = choice[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins +=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins +=1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won")
        user_wins +=1
    else:
         print("You lost")
         computer_wins+=1

print("You won" , user_wins , "times.")
print("Computer", computer_wins , "times.")  

if user_wins > computer_wins:
     print("WOAH! you won overall")       
else:
    print("You lost overall :(")  
    
print("***See you next time***")     