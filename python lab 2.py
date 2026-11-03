
cardValid = True
pinCorrect = 2222 
if cardValid:
    #if cardValid is true as assigned then:
    print("Access card accepted")
    #Ask user to input pin after card is accepted and convert to integer
    enterPin = int(input("Enter pin:"))
    #if pin entered is the same as the one assigned to the enterPin variable
    if pinCorrrect == enterPin:
      print("Access granted")
    else:
        #if pin entered is not the same as the one assigned to the enterPin variable
        print("Incorrect pin, try again")
else:
   #if cardValid is false as assigned then: 
 print("Invalid access card")
