elements=int(input('Enter the number of elements you want: '))
list_=[]
dictionary_={}

for i in range(1,elements+1):
    element=input(f'\nPlease enter the element {i}= ')
    list_.append(elements)
    dictionary_.setdefault(i,list_[i-1])

def messing_with_dictionary():
    print(f'\nThe keys are {dictionary_.keys()}')
    print(f'The values are {dictionary_.values()}')
    junk=int(input('\nEnter the key of the value you want to delete= '))
    if junk in dictionary_.keys():
        print('\n',dictionary_.pop(junk))
    else:
        print('\nSorry! The element is not there.')
    return()

messing_with_dictionary()
print(f'\n{dictionary_}')

print(f'\n {dictionary_.popitem()}')

print(f'\n{dictionary_}')