price = int(input('Enter amount of quantities :'))*100
print((price-(price//10)) if price>1000  else price)
