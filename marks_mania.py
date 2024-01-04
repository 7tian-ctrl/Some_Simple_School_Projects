
#les go

import math as m

print('\n We will first start by colecting the data.\n\n Please answer the questions:')

subjects=['Maths','Science','Social Science','Hindi','Information Technology','English']
marks=[]

for i in subjects:
   mark=float(input(f'\nPlease enter your marks(0-100) in {i}: '))
   if 0<=mark<=100:
      marks.append(mark)
   else:
      print('Please enter your marks between 0 to 100.')
    
dict_marks=dict(zip(subjects,marks))

percentage= sum(dict_marks.values())/6
print(f'\nCongrats ╰(*°▽°*)╯\n  You have scored {percentage}%')

if 60<=percentage<=100:
   print('\nHooray ヾ(≧▽≦*)o\n  You are in the I Division.')
   if dict_marks['Maths']>=75 and dict_marks['Science']>=75:
      print('\nYou are Eligible for Maths and Science Stream')
   else:
      print('\nSorry (ノへ￣、)\n You are not Eligible for Science stream')
elif 45<=percentage<=59:
   print('\nHooray ヾ(≧▽≦*)o\n  You are in the II Division.')
   if dict_marks['Maths']>=75 and dict_marks['Science']>=75:
      print('\nYou are Eligible for Maths and Science Stream')
   else:
      print('\nSorry (ノへ￣、)\n You are not Eligible for Science stream')
elif 33<=percentage<=44:
   print('\nHooray ヾ(≧▽≦*)o\n  You are in the III Division.')
   if dict_marks['Maths']>=75 and dict_marks['Science']>=75:
      print('\nYou are Eligible for Maths and Science Stream')
   else:
      print('\nSorry (ノへ￣、)\n You are not Eligible for Science stream')
else:
   print("\nSorry (┬┬﹏┬┬)\n  You didn't make it")
   