# Ask for the user's name and store it in a variable
name = input("What is your name? ")

# Ask for the user's age and store it in a variable
age = int(input("How old are you? "))

# Print a greeting using the name and age variables
print(f"Hello, {name}! You are {age} years old.")
#--------------------------------------------------------
# Ask for the length and width of the rectangle and store them as integers
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Print the result
print("The area of the rectangle is:", area)
#--------------------------------------------------------
# Ask for the temperature in Celsius and store it as a float
celsius = float(input("Enter temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the result rounded to two decimal places
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")