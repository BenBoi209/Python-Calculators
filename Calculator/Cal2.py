print('')
print('Welcome to my Python Cal2')
print('')

print('+ , - , / , * , % ')
operator = input('Select the logical operator from above: ')
print('')

if (operator == '+'):
        print('Sum: ',((int(input('First number: ')))+(int(input('Second number: ')))))
if (operator == '-'):
        print('Difference: ',((int(input('First number: ')))-(int(input('Second number: ')))))
if (operator == '/'):
        print('Quotient: ',((int(input('First number: ')))/(int(input('Second number: ')))))
if (operator == '*'):
        print('Product: ',((int(input('First number: ')))*(int(input('Second number: ')))))
if (operator == '%'):
        print('Reminder: ',((int(input('First number: ')))%(int(input('Second number: ')))))

print('')
print('Thank You')
     

