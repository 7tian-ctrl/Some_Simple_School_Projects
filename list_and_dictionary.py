
#les go

elements=int(input('Enter the number of elements you want: '))
list_=[]


for i in range(1,elements+1,1):
    element=input(f'\nPlease enter the element {i}= ')
    list_.append(element)


search_element=input('\nEnter the element you want to search= ')

def search(search_element):
    if search_element in list_:
        print(f'\n  -Your element was found! It is on position {list_.index(search_element) +1}')
    else:
        print('\nSorry! Your element was not found.')
    return()

search(search_element)






