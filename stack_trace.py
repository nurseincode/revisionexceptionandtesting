def func_a():
    print('Func A started')
    func_b()
    print('Func A ended')

def func_b():
    print('Func B started')
    func_c()
    print('Func B ended')

def func_c():
    print('Func C started')
    # try:
    result = 10 / 0
    # except ZeroDivisionError:
    #     print('Cannot divide by zero!')
    print('Func C ended')

# Main
func_a()