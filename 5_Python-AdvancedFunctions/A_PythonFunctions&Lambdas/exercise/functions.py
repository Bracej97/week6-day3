# Define a simple function
def greet():
    return "Hello, World!"

print(greet())

# Define a function with parameters
def add(a, b):
    return a + b

print(add(2, 3))

# Define a function with a default parameter
def personalised_greet(name = "guest"):
    return f"Hello, {name}!"

print(personalised_greet())
print(personalised_greet("Joe"))

# Define a function that accepts any number of arguments and keyword pair arguments
def print_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_info(1, 2, 3, name="Joe", town="Basingstoke")


#Lamda functions
# Define a basic lamda function
square = lambda x: x ** 2
print(square(2))

# Use a lamda function with map
squares = list(map(square, [1, 2, 3, 4]))
print(squares)

# Use a lamda function with filter
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(evens)

# Use a lamda function with sorted
sorted_list = sorted([(1, "apple"), (2, "cherry"), (3, "banana")], key=lambda x: x[1])
print(sorted_list)
