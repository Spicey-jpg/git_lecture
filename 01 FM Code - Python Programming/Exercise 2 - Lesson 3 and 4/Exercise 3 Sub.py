#Question 1
def greet():
    """Prints 'Hello, World!'"""
    print("Hello, World!")

greet()
#------------------------------------
#Question 2
def personalized_greeting(name):
    """Prints a personalized greeting."""
    print(f"Hello, {name}! Hope you’re having a fantastic day!")

personalized_greeting("William October")
#-------------------------------------
#Question 3
def square(number):
    """Returns the square of a number."""
    return number * number

result = square(5)
print("The square of 5 is:", result)
#------------------------------------
#Question 4
def rectangle_area(length, width):
    """Returns the area of the rectangle."""
    return length * width

area = rectangle_area(4, 5)

print("The area of the rectangle is:", area)
#------------------------------------
#Question 5
def apply_operation(func, number):
    """Applies the given function to the number."""
    return func(number)

def double(number):
    """Returns the double of the given number."""
    return number * 2

result_double = apply_operation(double, 7)
print("The double of 7 is:", result_double)

def square(number):
    """Returns the square of the given number."""
    return number * number

result_square = apply_operation(square, 3)
print("The square of 3 is:", result_square)
