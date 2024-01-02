
def pattern(name):
    length_name = len(name) 
    for i in range(length_name):
        print(name[0:i+1])
    return()

name=input('Please enter your name: ')
pattern(name)