a=int(input('Enter price of toy 1 :'))
b=int(input('Enter price of toy 2 :'))
c=int(input('Enter price of toy 3 :'))
s=0
if a>1000:
    s+=a-a//10
else:
    s+=a
if b>100:
    s+=b-b//5
else:
    s+=b
if c>500:
    s+=c-c//10
else:
    s+=c
print(s)

