UNITS = ['cm', 'm', 'kg', 'g', 'km', 'mm']

def intro():
    while True:
        print('------------------------------')
        print('Welcome to my Units Converter!')
        print('------------------------------')
        break

def convert_main():
    while True:
        #convert
        print('cm   m   kg   g   km   mm ')
        choose_convert = input('Enter the unit to convert from above: ').lower()
        if choose_convert in UNITS:
            selected_unit_to_convert = choose_convert
            unit = float(input(f"Enter {selected_unit_to_convert}: "))
        else:
            print('_________________________________')
            print('Enter something valid. Try Again!')
            print('---------------------------------')
            continue

        #converted
        print('')
        print('cm   m   kg   g   km   mm ')
        choose_converted = input(f'Enter the unit to convert {selected_unit_to_convert} from above: ').lower()
        if choose_converted == selected_unit_to_convert:
            print('-----------------------------------')
            print("You can't convert to the same unit. Try Again!")
            print('-----------------------------------')
            continue
        else:
            if choose_converted in UNITS:
                selected_unit_to_converted = choose_converted
            else:
                print('_________________________________')
                print('Enter something valid. Try Again!')
                print('---------------------------------')
                continue

        if selected_unit_to_convert == 'kg' and selected_unit_to_converted == 'g':
            result = unit * 1000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'km' and selected_unit_to_converted == 'm':
            result = unit * 1000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'g' and selected_unit_to_converted == 'kg':
            result = unit / 1000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'm' and selected_unit_to_converted == 'km':
            result = unit / 1000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'm' and selected_unit_to_converted == 'cm':
            result = unit * 100
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'cm' and selected_unit_to_converted == 'm':
            result = unit / 100
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'cm' and selected_unit_to_converted == 'mm':
            result = unit * 10
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'mm' and selected_unit_to_converted == 'cm':
            result = unit / 10
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'cm' and selected_unit_to_converted == 'km':
            result = unit / 100000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'km' and selected_unit_to_converted == 'cm':
            result = unit * 100000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'km' and selected_unit_to_converted == 'mm':
            result = unit * 1000000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'mm' and selected_unit_to_converted == 'km':
            result = unit / 1000000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'mm' and selected_unit_to_converted == 'm':
            result = unit * 1000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        elif selected_unit_to_convert == 'm' and selected_unit_to_converted == 'mm':
            result = unit / 1000
            print(f"{unit} {selected_unit_to_convert} is: ",str(result),f" {selected_unit_to_converted}" )
            break
        else:
            print('-----------------------------------------------------------------------------------------')
            print(f"You can't convert {selected_unit_to_convert} to {selected_unit_to_converted}. Try Again!")
            print('-----------------------------------------------------------------------------------------')
            continue

def main():
    while True:
        intro()
        convert_main()

        print('')
        print('Do you want to exit this application? (yes/no) ')
        continue_using_application = input('>')
        if continue_using_application != 'no':
            print('----')
            print('Bye!')
            print('----')
            quit()



main()
