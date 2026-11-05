import random
playerInput = "y"
#if player inputs y then restart the entire loop body
while playerInput == "y":
#Generate random number between 1 and 3 inclusive
 chosen=random.randint(1,3)
#convert chosen number to letter
 if chosen==1:
    computer="r"
 elif chosen==2:
    computer="p"
 else:
    computer="s"
    #Ask player choice
 player=input("Enter rock(r),scissors(p) or paper(s)?:").lower()
#display both player and computer choices
 print(computer)
 print(player)
#determine winner
 if computer==player:
    print("DRAW")
 elif ((computer == "r" and player == "p") or 
     (computer == "p" and player == "s") or 
     (computer == "s" and player == "r")): 
     print("Player Wins")
 else:print("Computer Wins") 
 playerInput=input("Do you want to play again? Enter y/n:")
 #if the user makes the condition to repeat false then print:
print("Thanks for playing!")