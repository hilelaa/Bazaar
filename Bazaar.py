a=int(input('Enter amount u want to bet'))

import random
x=random.randint(1,6)
print(x)
y=random.randint(1,6)
print(y)
z=x+y
print(z)
if z<=6:
 print(z)
 print('Congrats Small bazaar')
elif z==7:
 print(z)
 print('Congrats Lucky')
elif z>7:
 print(z)
 print('Congrats Big bazaar')