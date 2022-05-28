## Please make sure to uppercase all entries and use only letters- no other characters! Click 'enter' 

import random
myList = ["Rock" , "Scissors" , "Paper"]
# comp = random.choice(myList)
numWinsComputer = 0
numWinsGuest = 0
firstToWin = 3

keep_going = True

# The function           
def guestWins(ask_user, comp):
    global numWinsComputer
    global numWinsGuest
    #print("inside function with ", ask_user, " ", comp)
    if ask_user == "Paper":
       print("You threw" , ask_user , "and the computer chose" , comp ,)
       if comp == "Rock":
            print("  Paper beats rock! Good job!")
            numWinsGuest = numWinsGuest+1
       else:
            print("  Scissors beat Paper! Better luck next time!")
            numWinsComputer = numWinsComputer+1


    elif ask_user == "Rock":
        print("  You threw" , ask_user , "and the computer chose" , comp ,)
        if comp == "Paper":
            print("  Paper beats Rock! Sorry!")
            numWinsComputer = numWinsComputer+1
        else:
            print("  Rock beats Scissors! Good job!")
            numWinsGuest = numWinsGuest+1
        

    elif ask_user == "Scissors":
        print("   You threw" , ask_user , "and the computer chose" , comp ,)
        if comp == "Paper":
            print("  Scissors beats Paper! Great job!")
            numWinsGuest = numWinsGuest+1
        else:
            print("  Rock beats Scissors! Try again!")
            numWinsComputer = numWinsComputer+1
        


while keep_going == True:
    comp = random.choice(myList)
    print('')
    print("Current Score :Computer ", numWinsComputer,
                             "Guest ", numWinsGuest)
    ask_user = input("Choose to throw one: Rock, Paper, or Scissors: ")
    ask_user = ask_user.strip()

    if ask_user == comp:
        print("You threw" , ask_user , "and the computer also chose" , comp ,)
        print("It's a tie for now!")

    else:
        guestWins(ask_user, comp)
     
    if(numWinsComputer == firstToWin):
        print('Game Over - you lose!!!')
        keep_going = False
    elif numWinsGuest == firstToWin:
        print('You Win !! Congrats !!!')
        keep_going = False
    else:
        play_again = input("Play again? ")
        if play_again.lower() == "no":
            keep_going = False
        elif play_again.lower() == "yes":
            keep_going = True
        else:
            keep_going = False


print('')
print("Final Score : Computer ", numWinsComputer, "   Guest ", numWinsGuest)