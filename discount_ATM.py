
#les go

pin=int(input('Please enter a pin: '))
current_balance=0.00

print('Menu')
print('1. Check Balance')
print('2. Withdraw')
print('3. Deposit')
print('4. Change Pin')

while 1>0:

    choice=int(input('\nEnter what you want to do(1-4)= '))

    if choice==1:
        lock=int(input('\n  Please enter your pin: '))
        if lock==pin:
            print(f'\nWelcome to our ATM! ^_^\n Your Current Balance is {current_balance}') 
        else:
            print('\nOops! Incorrect pin (┬┬﹏┬┬)\n\n Try Again!')
 
    elif choice==2:
        lock=int(input('\n  Please enter your pin: '))
        if lock==pin:
            withdraw_amount=float(input('Enter the amount you want to withdraw: '))
            if withdraw_amount<=current_balance:
                print(f"\nHere's your money ヾ(≧▽≦*)o \nYou have currently {current_balance-withdraw_amount} left in your account.")
            else:
                print(f"\nA friendly reminder, You're Broke (￣y▽,￣)╭ ")
                print(f"\n  You're short by {withdraw_amount-current_balance}.")
        else:
            print('\nOops! Incorrect pin (┬┬﹏┬┬)\n\n Try Again!')
 
    elif choice==3:
        lock=int(input('\n  Please enter your pin: '))
        if lock==pin:
            deposit_amount=float(input('Enter the amount you want to deposit: '))
            print(f'\nCongrats ☆*: .｡. o(≧▽≦)o .｡.:*☆\nYou have successfully deposited your money.\nYou have currently {current_balance+deposit_amount} in your account.')
            current_balance= current_balance + deposit_amount
        else:
            print('Oops! Incorrect pin (┬┬﹏┬┬)\n\nTry Again!')
    
    elif choice==4:
        lock=int(input('\n  Please enter your pin: '))
        if lock==pin:
            new_pin=int(input('Please enter the new pin: '))
            pin=new_pin
            print('\n...Your pin has been changed.(*/ω＼*)')
        else:
            print('Oops! Incorrect pin (┬┬﹏┬┬)\n\n Try Again!')
    
    else:
        print('Please enter a choice from 1 to 4.')