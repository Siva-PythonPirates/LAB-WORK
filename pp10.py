a=int(input('Dist :'))
if a>=1 and a<=50:
    print('Fare :',a*8)
elif a>50 and a<=80:
    print('Fare :',a*10)
else:
    print('Fare :',a*12)
