
#les go

import math as m

x=float(input('Enter a Number: '))

def progression_sum(x):
    answer=0
    for i in range(1,11):
        answer= answer + x**(i)/m.factorial(i)
    print(f'\n  Sum= {(answer)}')
    return()

progression_sum(x)