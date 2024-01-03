
#les go

elements=int(input('Enter the number of elements you want: '))
list_=[]
dictionary_={}

for i in range(1,elements+1,1):
    element=input(f'\nPlease enter the element {i}= ')
    list_.append(element)
    dictionary_.setdefault(i,list_[i-1])

search_element=input('\nEnter the element you want to search= ')

def search(search_element):
    if search_element in list_:
        print(f'\n  -Your element was found! It is on position {list_.index(search_element) +1}')
    else:
        print('\nSorry! Your element was not found.')
    return()

search(search_element)

def messing_with_dictionary():
    print(f'\nThe keys are {dictionary_.keys()}')
    print(f'The values are {dictionary_.values()}')
    junk=int(input('\nEnter the key of the value you want to disappear= '))
    if junk in dictionary_.keys():
        print('\n',dictionary_.pop(junk))
    else:
        print('\nSorry! The element is not there.')
    return()

messing_with_dictionary()
print(dictionary_)