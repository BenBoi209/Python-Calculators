print('Welcome to my Python calculator')
print('+ , - , * , / , %')

operation = input('Select the operation from above : ')
if (operation == '+'):
    print('Addition')
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    sum = num1 + num
    print('Sum: ',sum)

if (operation == '-'):
    print('Subtraction')
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    difference = num1 - num2 
    print('Difference: ',difference)

if (operation == '*'):
    print('Multiplication')
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    product = num1 * num2 
    print('Product: ',product)

if (operation == '/'):
    print('Division')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    quotient = num1 / num2
    print('Quotient: ',quotient)

if (operation == '%'):
    print('Reminder')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    reminder = num1 % num2
    print('Reminder: ',reminder)

print('Thank You For using My Python Calculator')





