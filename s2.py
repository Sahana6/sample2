n=int(input("enter a number\n"))
if n<9 and n>0:
    for i in range(n,9):
        print("%d%s%d"%(i,":",i*i))
else:
    print("enter a positive number less than 9")




