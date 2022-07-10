def first_function():
    print("This is my first function.")

def Second_function(func):
    print("This is my second function.")
    return func

my_func = Second_function(first_function)
my_func()

