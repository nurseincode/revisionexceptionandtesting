def convert_to_integer(value):
    try: 
        10 / 0 
        result = int(value)
        print(f'Conversion successful! Result: {result}')
    except ValueError:
        print('Conversion failed. Please enter a valid integer.')
    else:
        print('Else invoked')
    finally:
        print('Close any open resources')


# User input

spam = input('Enter a number to convert into an integer: ')
convert_to_integer(spam)


