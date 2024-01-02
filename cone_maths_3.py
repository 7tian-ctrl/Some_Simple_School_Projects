
#import math

import math as math 

radius= float(input('Please enter the Radius= '))
height= float(input('Please enter the Height= '))

curve_height= math.sqrt((radius)**2 + (height)**2) 

print(f'\nC.S.A= {3.14*radius*curve_height}')              #CSA of cone= pi*r*l

print(f'T.S.A= {3.14*radius*(curve_height+radius)}')       #TSA of cone= pi*r*(l+r)

print(f'Volume= {(3.14*(radius**2)*height)/3}')     #Volume of cone=1/3*(pi*r_squared*h)