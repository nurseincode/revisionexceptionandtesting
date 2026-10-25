def convert_to_integer(value):
    try: 
        10 / 0 
        result = int(value)
        print(f'Conversion successful! Result: {result}')
    except ValueError:
        print('Invalid input. Please enter a whole number, such as 5 or 12.')
    except ZeroDivisionError:
        print('A division error occurred. Please try again!')
    else:
        print('Else invoked')
    finally:
        print('Close any open resources')


# User input

spam = input('Enter a number to convert into an integer: ')
convert_to_integer(spam)


