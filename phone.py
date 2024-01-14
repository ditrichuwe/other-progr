
for i in range(5):
    money=int(input("How much money do you have?"))
    if money>=20:

        if money>=20 and money<=50:
              print("you can buy a nokia")
        elif money>=51 and money<=100:
              print("you can buy a xiomi")
        elif money>=100 and money<=500:
              print("you can buy samsung")
        else:
              print("you can buy every phone")
    else:
        print("you cant buy a phone")
