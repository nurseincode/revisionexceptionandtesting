def convert_to_integer(value):
    try: 
        # 10 / 0 
        result = int(value)
        print(f'Conversion successful! Result: {result}')
        return result
    # except ValueError:
    #     print('Invalid input. Please enter a whole number, such as 5 or 12.')
    # except ZeroDivisionError:
    #     print('A division error occurred. Please try again!')
    # except Exception as e:
    #     print(f'An unexpected error occurred: {e}')
    except ValueError:
        raise
    else: # only happens if no exceptions occurred
        print('Else invoked')
    finally: # happens no matter what
        print('Close any open resources')


# User input

if __name__ == "__main__":
    spam = input('Enter a number to convert into an integer: ')
    convert_to_integer(spam)


