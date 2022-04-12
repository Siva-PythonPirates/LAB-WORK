a=int(input('No :'))
flag=0
for i in range(2,a//2):
    if i%2==0:
        flag=1
    else:
        flag=0
if flag==0:
    print('Prime')
else:
    print('Not a prime')
    
