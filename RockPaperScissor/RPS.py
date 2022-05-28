import random
myList = ["Rock" , "Scissors" , "Paper"]
comp = random.choice(myList)

keep_going = True



while keep_going == True:
    comp = random.choice(myList)
    ask_user = input("Choose to throw one: Rock, Paper, or Scissors: ")
    ask_user = ask_user.strip()

    if ask_user == comp:
        print("You threw" , ask_user , "and the computer also chose" , comp ,)
        print("It's a tie for now!")

    elif ask_user == "Paper":
       print("You threw" , ask_user , "and the computer chose" , comp ,)
       if comp == "Rock":
            print("Paper beats rock! Good job!")
       else:
            print("Scissors beat Paper! Better luck next time!")


    elif ask_user == "Rock":
        print("You threw" , ask_user , "and the computer chose" , comp ,)
        if comp == "Paper":
            print("Paper beats Rock! Sorry!")
        else:
            print("Rock beats Scissors! Good job!")
        

    elif ask_user == "Scissors":
        print("You threw" , ask_user , "and the computer chose" , comp ,)
        if comp == "Paper":
            print("Scissors beats Paper! Great job!")
        elif comp == "no":
            print("Rock beats Scissors! Try again!")
            
    play_again = input("Play again? ")
   
    if play_again == "No":
        keep_going = False
    else:
        keep_going = True
    
            

        
