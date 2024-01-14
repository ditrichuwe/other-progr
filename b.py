print("ita a moneybox programm")
saved_euros=0

your_amount=int(input("How much money do you have?"))
amountOfMoneyYouSave=int(input("How much moey do you want to save per day?"))
your_amountOfDays=int(input("How much days do you wnt to save the money?"))

for i in range(1,your_amountOfDays+1):
        your_amount=your_amount+amountOfMoneyYouSave
        print (f"Current day {i}")
        print("your amount "+str(your_amount))
                      
