def decorator (original_func):
    print('from decorator')

    def wrapper():
        print(f'Wrapper excuted before {original_func. __name__} ()')

        return original_func()
    return wrapper

def print_something():
    print('print_something is being ran!')

p=decorator(print_something)
p()
