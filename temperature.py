
for i in range(10):
    temperature=int(input("What temperature is now?"))
    if temperature>=-20 and temperature<=10:
        print('Its cold outside')
    if temperature>=11 and temperature<=25:
        print('Its warm outside')
    if temperature>25:
        print('Its hot outside')
    
