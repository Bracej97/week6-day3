my_list = [1, 2, 3, 4, 5]

# Create a function that iterates over a given list using iter() and next() and handles the StopIteration
def iterator(list):
    iterate = iter(list)
    try:
        while True:
            print(next(iterate))
    except StopIteration:
        print("This is the end of the list")

iterator(my_list)

# List comprehension to create a new list with the square of the numbers
squares = [x**2 for x in my_list]
print(squares)

# Set comprehension to create a set of unique characters from a string
uniques = {x for x in "My dog needs to go to the vet"}
print(uniques)

#Dictionary comprehension to create a dictionary mapping numbers to their squares
square_dict = {x: x**2 for x in my_list}
print(square_dict)

# For loop iterating over square list
for numb in squares:
    print(numb)

# While loop
x = 1
sum = 0
while x <= 100:
    sum += x
    x += 1
    print(sum)

# While loop with a break
y = 1
sum = 0
while y <= 100:
    sum += y
    y += 1
    print(sum)
    if sum > 150:
        break
