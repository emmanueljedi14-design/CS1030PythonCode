import random
chosen=random.randint(1,3)
if chosen==1:
    computer="r"
elif chosen==2:
    computer="p"
else:
    computer="s"
player=input("Enter rock(r),scissors(s) or paper(p)?:").lower()
print(computer)
print(player)
if computer==player:
    print("DRAW")
elif ((computer == "r" and player == "p") or 
     (computer == "p" and player == "s") or 
     (computer == "s" and player == "r")): 
     print("Player Wins")
else:print("Computer Wins") 