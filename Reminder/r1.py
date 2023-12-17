import time

def reminder_func():
    while True:
        print('Enter the reminder below: ')
        reminder = input('> ')
        if reminder.isdigit():
            print('--------------------------------------------------')
            print("You can't enter a number as a reminder. Try Again!")
            print('--------------------------------------------------')
            continue
        else:
            number_of_secs = input('Enter the time for you to get reminded (in secs): ')
            if number_of_secs.isdigit():
                number_of_secs = int(number_of_secs)
                for i in range(number_of_secs + 1):
                    time.sleep(1)
                    print(i)
                    if i == number_of_secs:
                        print('--------------------------------------------')
                        print('Your Reminder: ')
                        print(reminder)
                        print('--------------------------------------------')
            else:
                print('--------------------------')
                print('Enter a number. Try Again!')
                print('--------------------------')
                continue
                
            break
def main():
    while True:
        reminder_func()

        print('Do you want to quit this application? (yes/no)')
        using_application = input('> ')
        if using_application != 'no':
            print('----')
            print('Bye!')
            print('----')
            quit()

main()
