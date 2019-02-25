s=input("Input a string")
d=0
a=0
s=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        a=a+1
    else:
        pass
print("number of alphabets is", a)
print("number of digits is", d)