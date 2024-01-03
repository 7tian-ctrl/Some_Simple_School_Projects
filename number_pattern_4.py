
#lets go

num=int(input('Please enter a natural number:'))

for i in range(1,num+1):
    for j in range(1,i+1):
      print(''*(num-i),j,end='')
    print()
    


