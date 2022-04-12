a=int(input('NO '))
b=a
s=0
for i in range(len(str(a))):
    s+=(a%10)**3
    a=a//10
if s==b:
    print('True')
else:
    print('False')
