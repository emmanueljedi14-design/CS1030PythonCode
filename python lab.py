score = int(input('Enter your exam score:'))
if score >= 50:
    print("You passed!")
    if score >= 80:
     print("You earned an A!")
    else:
      print('You passed but did not earn an A.')  
else:
    print('You failed!!')