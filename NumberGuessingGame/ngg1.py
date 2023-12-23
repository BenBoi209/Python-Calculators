import random

user_tries = 0

def main():
    global user_tries
    while True:
        com_guess = random.randint(1,10)
        user_guess = input('Enter your guess (1 - 10)/(Q to quit) : ')
        if user_guess == 'q' or user_guess == 'Q':
            print('----')
            print('Bye!')
            print('----')
            quit()
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess != com_guess:
                user_tries += 1
                print('You Guessed Wrong!')
                continue
            else:
                print('You Guessed Right!')
                print(f'It took you {user_tries} tries to guess the right number.')
        else:
            print('------------------------------')
            print('Enter a number between 1 - 10.')
            print('------------------------------')
            continue
        break

if __name__ == '__main__':
    main()
        
