import random

player_points=100

while player_points>0:
    
    player_number=int(input("type in a number between 2 and 12"))
    players_bet=int(input("what amount of points do you want to bet"))

    print("computer is throwing the dices")
    computers_dice1=random.randint(1,6)
    computers_dice2=random.randint(1,6)
    print(computers_dice1)
    print(computers_dice2)

    if (computers_dice2+computers_dice1)<7 and player_number<7:
        player_points=player_points+players_bet
        print("your balance is now "+str(player_points))

    elif (computers_dice2+computers_dice1)>7 and player_number>7:
        player_points=player_points+players_bet
        print("your balance is now "+str(player_points))

    elif (computers_dice2+computers_dice1)==player_number:
        player_points=player_points+players_bet*4
        print("your balance is now "+str(player_points))

    else:
        player_points=player_points-players_bet
        print("your balance is now "+str(player_points))

    if player_points==0:
        print("you lose")

    answer=input("do you want to continue? ")
    
    if answer=="no":
        break


        
