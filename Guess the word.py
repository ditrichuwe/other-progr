##MFA=["Running","Swimming","Pythony"]
##print(MFA[2])
##MFA.append("sleeping")
##print(MFA)
##MFA.append("eating")
import random

letters=[]
words=['keyboard','football','tournament','water']
secretword=random.choice(words)
attempts=10

while attempts>0:
    victory=True
    letter=input("Type in a letter")
    if letter not in secretword:
        attempts=attempts-1
        print(str(attempts))
    letters.append(letter)
    for char in secretword:
        if char in letters:
            print (char)
        else:
            print ("*")
            victory=False
    if victory==True:

       print("You Win")
       break
