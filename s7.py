n =input("enter a sentence")
l=0
u=0
for c in n:
    if c.isupper():
        u=u+1
    elif c.islower():
        l=l+1
    else:
        pass
print("no. of uppercase letters %d"%u)
print("no. of lowercase letters %d"%l)