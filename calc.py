def calculate():
    operation = input('''
Please type the math operation you would like to complete:
+ for addition
- for substraction
* for multiplication
/ for division
''')

#A function to ask user if they want to use the calculator again
def again():
    calc_again = input(''' Do you want to calculate again? Type Y for Yes or N for No ''')

    if calc_again.upper() == 'Y': # To accept both y and Y as a yes
        calculate()
    elif calc_again.upper() == 'N': # To accept both n and N as a no
        print("see you later.")
    else:
        again()

calculate()

num1=int(input('Enter your first number:'))
num2=int(input('Enter your second number:'))

if operation == '+':#addition
    print('{} + {} ='.format(num1, num2))
    print(num1+num2)

elif operation == '-':#substraction
    print('{} - {} ='.format(num1, num2))
    print(num1-num2)

elif operation == '*':#multiplication
    print('{} * {} ='.format(num1, num2))
    print(num1*num2)

elif operation == '/':#division
    print('{} / {} ='.format(num1, num2))
    print(num1/num2)
    
else:
    print('Please enter a valid operator')

calculate()