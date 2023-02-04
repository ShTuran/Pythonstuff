name = input("Type your name: ")
print("Welcome ", name , "to adventure")

answer = input ("You are around the sea, type swim to swim, type go to go. ").lower()

if answer == "swim":
    print("There was alligator in the sea. You lost!")
    
elif answer == "go":
    answer = input("You came to castle, type lift to lift, type see to look around. ")
    
    if answer == "lift":
        print("This castle was protected by a king and no one allowed to enter, they killed you. You lost!")
    elif answer == "see":
        answer=input("You meet a stranger. And she told you that she knew gold place but she need help. Type help to help her, or not help. ")
        
        if answer == "help":
            print("You and her are found the gold and now you are rich. You won!")
        elif answer == "not help":
            print("It was your only choice. You lost!")
        else:
        
            print("Not a valid option. You lost!")
    else:
        print("Not a valid option!")
      
        
else:
    print("Not a valid option!")
    