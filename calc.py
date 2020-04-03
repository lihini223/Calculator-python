def calculate():
    operation = input('''
Please type the math operation you would like to complete:
+ for addition
- for substraction
* for multiplication
/ for division
''')

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