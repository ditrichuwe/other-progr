Cost=int(input("How much did your food cost?"))
print("tax=")
tax=Cost/10
print(tax)
print("service=")
service=Cost/20
print(service)
print("Total "+str(round(Cost*1.15,3)))
