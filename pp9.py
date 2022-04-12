l=[int(input('NO 1:')),int(input('NO 2:')),input('operator :')]
if l[-1]=='+':
    print(l[0]+l[1])
elif l[-1]=='-':
    print(l[0]-l[1])
elif l[-1]=='*':
    print(l[0]*l[1])
elif l[-1]=='/':
    try:print(l[0]/l[1])
    except:ZeroDivisionError,print('Zero division not posible')
elif l[-1]=='%':
    print(l[0]%l[1])
elif l[-1]=='//':
    print(l[0]//l[1])
else:
    print('Invalid')
