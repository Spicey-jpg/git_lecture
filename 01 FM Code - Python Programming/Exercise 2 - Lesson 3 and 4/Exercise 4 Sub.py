# Question 1: Using a for loop with a list

# TODO: Create a list of fruits

# TODO: Use a for loop to print each fruit in the list
fruits=("apple", "pear", "banana","orange", "watermelon")
for fruit in fruits:
    print(fruit)



#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1



#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()
for number in range(1, 11):
# TODO: Use a for loop to print the first 10 square numbers
    print(number ** 2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["red", "green", "purple", "blue" ]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(colors))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print(math_operations.add(10, 20))       
print(math_operations.subtract(10, 20))  
print(math_operations.multiply(10, 20))  
print(math_operations.divide(10, 20))    
print(math_operations.divide(10, 20))


# TODO: Use a while loop to create a simple calculator
def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Choose a operator (1-5): ")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter a second number: "))

        if choice == '1':
            print(f"Result: {math_operations.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {math_operations.sub(num1, num2)}")
        elif choice == '3':
            print(f"Result: {math_operations.mult(num1, num2)}")
        elif choice == '4':
            print(f"Result: {math_operations.div(num1, num2)}")
        else:
            print("error, please try again.")

calculator()
