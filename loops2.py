summ=0
summa=0
for i in range(1899,3159):
    if i %3==0 and i %7==0 and i %5.5==0:
        summ=summ+i
    else:
        summa=summa+i
print(summ)
print(summa)
