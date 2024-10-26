# Create a try and except block
try:
    print(x)
except NameError:
    print("You need to define x as there is a NameError")
except:
    print("Something else went wrong")
finally:
    print("I will run anyway")

x = "I have been defined"
try:
    print(x)
except:
    print("You need to define x")
else:
    print("nothing went wrong")
finally:
    print("I will run anyway")

num1 = 10
num2 = 100

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def get_age(self):
        print(f"{self.name} is {self.age} years old!")

dog1 = Dog("buddy", 2)

dog1.bark()
dog1.get_age()
