l=[int(input('a :')),int(input('b :')),int(input('c :')),int(input('d :')),int(input('k :')),int(input('x :'))]
if l[-2]<l[-1]:
    print((l[0]*l[-1]**3)-(l[1]*l[-1]**2)+(l[2]*l[-1])-l[3])
elif l[-1]==0:
    print(0)
else:
    print(-(l[0]*l[-1]**3)+(l[1]*l[-1]**2)-(l[2]*l[-1])+l[3])
