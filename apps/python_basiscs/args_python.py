def print_inputs(arg1, *argv):
    print('------------------')
    print(arg1)
    print('------------------')
    for arg in argv:
        print(arg)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} - {value}')


def print_arg_kwarg(*args, **kwargs):
    print('++++++++++ args +++++++++++')
    for arg in args:
        print(arg)
    print('++++++++++ kwargs +++++++++++')
    for key, value in kwargs.items():
        print(f'{key} - {value}')


print_inputs('this', 'is', 'charan', 'testing', '*args')
print_inputs('this is charan testing *args'.split())

print_kwargs(input_val1='something', input_valuu2='fucking something')
print_arg_kwarg('this', 'is', 'charan', 'testing', '*args', input_val1='something', input_valuu2='fucking something')
