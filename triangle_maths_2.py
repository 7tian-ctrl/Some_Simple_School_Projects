
#start


sides_list=[]
for i in range(1,4):
    side=float(input(f'Please enter side {i}: '))
    sides_list.append(side)


def type_of_triangle():
    if sides_list[0]==sides_list[1]==sides_list[2]:
        print('\nIt is an Equilateral triangle.')

    elif sides_list[0]==sides_list[1] or sides_list[1]==sides_list[2] or sides_list[2]==sides_list[0]:
        print('\nIt is an Isosceles triangle.')

    else:
        print('\nIt is a Scalene Triangle.')
    return()

type_of_triangle()

def right_angled_or_not():
    sorted(sides_list)
    if (sides_list[0])**2 + (sides_list[1])**2 == (sides_list[2])**2:
        print('\nIt is Right-angled.')
    else:
        print('\nIt is not Right-angled.')

right_angled_or_not()

def perimeter_and_area():
    sorted(sides_list)
    area = (sides_list[0]*sides_list[1])/2
    perimeter = sum(sides_list)
    print(f'\nPerimeter= {perimeter}\nArea= {area}')
    return()

perimeter_and_area()