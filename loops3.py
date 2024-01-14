from math import pi

while True:
    radius=int(input("type in the radius"))
    print(round(radius*2*pi,3))
    answer=input("do you want to go? ")
    
    if answer=="no":
        break
    
