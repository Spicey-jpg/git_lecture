# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Add a fruit to the end of the list
fruits.append("date")

# Insert a fruit at the beginning of the list
fruits.insert(0, "mango")

# Remove a fruit from the list
fruits.remove("banana")

# Print the modified list
print("Modified list of fruits:", fruits)
#-------------------------------------
# Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared
squared_numbers = [num**2 for num in numbers]

# Find the sum of the original numbers
total_sum = sum(numbers)

# Calculate the average of the original numbers
average = total_sum / len(numbers)

# Print the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Sum of original numbers:", total_sum)
print("Average of original numbers:", average)
#------------------------------------------
# Create a dictionary of countries and their capitals
countries_and_capitals = {
    "France": "Paris",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Germany": "Berlin"
}

# Add a new country-capital pair
countries_and_capitals["Spain"] = "Madrid"

# Update the capital of an existing country
countries_and_capitals["Germany"] = "Munich"

# Remove a country-capital pair
del countries_and_capitals["Italy"]

# Print the modified dictionary
print("Modified dictionary of countries and capitals:", countries_and_capitals)
#-------------------------------------------
# Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "date": "brown",
    "grape": "purple"
}

# Print all the fruits (keys)
print("Fruits (keys):", fruit_colors.keys())

# Print all the colors (values)
print("Colors (values):", fruit_colors.values())

# Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}")

# Check if a fruit is in the dictionary and print its color
fruit_to_check = "banana"
if fruit_to_check in fruit_colors:
    print(f"The color of {fruit_to_check} is {fruit_colors[fruit_to_check]}")
else:
    print(f"{fruit_to_check} is not in the dictionary")
