import random
import string

alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

def generate_password_user_details(len):
    rp = userName + favFood + bornYear + country
    return ''.join(random.choice(rp) for _ in range(len))

def generate_password_default(len):
    rp = alphabets + numbers + symbols
    return ''.join(random.choice(rp) for _ in range(len))

while True:
    print('Welcome to Random Password Generator')
    len = int(input('Enter the length of the password: '))

    def generate_password_user_details(len):
        rp = userName + favFood + bornYear + country
        return ''.join(random.choice(rp) for _ in range(len))
    
    print('Do you want to generate a random password with your details?')
    userDetails = input('>').lower()
    if userDetails == 'yes':
        userName = input('Enter your name: ').lower()
        favFood = input('Enter your favourite food: ').lower()
        bornYear = input('In which year were you born? ')
        country = input('Enter your country: ').lower()
        list_to_gen = [userName, favFood, bornYear, country]
        generated_password = generate_password_user_details(len)
        print('Generated Password: ',generated_password)
    elif userDetails == 'no':
        generated_password = generate_password_default(len)
        print('Generated Password: ',generated_password)
    else:
        print('Enter something valid nextime.')
        break

    print('Do you want to continue using Random Password Generator (yes/no) ?')
    proceed = input('>').lower()
    if proceed == 'yes':
        continue
    else:
        break
    
print('Good Bye!')



