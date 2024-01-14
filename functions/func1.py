
def square():
    side1=int(input("type in a side of the first square"))
    square=side1*side1
    print(square+1.5)

def triangle():
    sides=input("type in all the sides ").split(" ")
    side1=int(sides[0])
    side2=int(sides[1])
    side3=int(sides[2])
    perimetor=side1+side2+side3
    print(perimetor)


def sommeNumbers(counter):
    result=0
    for i in range(counter):
        number=int(input("type in a number"))
        result=number+result
    print(result)

sommeNumbers(8)




