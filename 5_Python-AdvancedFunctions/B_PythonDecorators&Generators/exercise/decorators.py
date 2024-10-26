# Define a simple decorator function
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Apply the decorator to the function
@simple_decorator
def greet():
    print("Hello!")

greet()

# Define a decorator that accepts args to the function
def less_simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@less_simple_decorator
def personalised_greet(name="Guest"):
    print(f"Hello, {name}!")

personalised_greet()
personalised_greet("Joe")
