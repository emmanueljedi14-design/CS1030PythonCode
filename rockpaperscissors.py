player=input("Enter rock(r),scissors(s) or paper(p)?:")
print(player)
computer="s"
if computer==player:
    print("DRAW")
elif ((computer == "r" and player == "p") or 
     (computer == "p" and player == "s") or 
     (computer == "s" and player == "r")): 
     print("Player Wins")
else:print("Computer Wins") 