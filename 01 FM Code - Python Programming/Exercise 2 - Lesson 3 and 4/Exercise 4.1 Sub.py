def check_attendance(students, absentees):
    """Returns a list of students who are absent."""

# List of students
students = ["William", "Uzair", "Charles", "Elias"]

# List of absentees
absentees = ["Juan", "People"]

# Call the 'check_attendance' function and print the result
absent_students = check_attendance(students, absentees)
print("Absent students:", absent_students)
#----------------------------------------------------
def calculate_average_grade(grades):
    """Calculates the average grade of the class."""
    total = sum(grades.values())
    count = len(grades)
    return total / count

# Dictionary of student grades
grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

# Call the 'calculate_average_grade' function and print the result
average_grade = calculate_average_grade(grades)
print("The average grade of the class is:", average_grade)
#--------------------------------------------------------
# Define the 'operation_selector' function
def operation_selector(operation):
    """Returns a function that adds or multiplies two numbers based on the operation specified."""
    def add(a, b):
        return a + b
    
    def multiply(a, b):
        return a * b
    
    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply
    else:
        return None

# Use 'operation_selector' to get the "add" function and call it to add 4 and 6
add_function = operation_selector("add")
result_add = add_function(4, 6)
print("4 + 6 =", result_add)

# Use 'operation_selector' to get the "multiply" function and call it to multiply 3 and 7
multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print("3 * 7 =", result_multiply)
#-------------------------------------------------
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    """Calculates the total cost of fuel for the trip."""
    return (distance / fuel_efficiency) * fuel_price
# Create a dictionary with grocery items as keys and their quantities in stock as values
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# Use a for loop to print each item and its quantity in stock
for item, quantity in grocery_inventory.items():
    print(f"{item}: {quantity} in stock")

# Calculate and print the total number of items in stock (sum of all values in the dictionary)
total_items = sum(grocery_inventory.values())
print(f"Total number of items in stock: {total_items}")
#----------------------------------------------
correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter your PIN: ")
    
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
        
if attempts == 3:
    print("Account Locked")
#--------------------------------------------------
import random

# List of 10 student scores
scores = [random.randint(0, 100) for _ in range(10)]

# Calculate total score using a for loop
total_score = 0
for score in scores:
    total_score += score

# Calculate average score
average_score = total_score / len(scores)

# Print the total and average scores
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")

# Bonus: Print a congratulatory message if the average is above 75
if average_score > 75:
    print("Congratulations! The class performed exceptionally well.")
#----------------------------------------------
import random

# List of participants
participants = ["Adam", "Eve", "William", "Rhonda", "Connor",
                "William Senior", "Rodney", "Jasmane", "Jayden", "Caitlin",
                "Jaydene", "Nadine", "Cullen", "Elrich", "Storm",
                "Phoenix", "Samsung", "Huawei", "Oppo", "Hisense"]

# Randomly select 5 people from the participants list
selected_team = random.sample(participants, 5)

# Print the names of the selected team members
print("Selected team members are:", selected_team)
#----------------------------------------------
# fitness_tracker.py

def walk_calories(distance_km):
    """Calories burned per km walking: 50"""
    return distance_km * 50

def run_calories(distance_km):
    """Calories burned per km running: 100"""
    return distance_km * 100

def cycle_calories(distance_km):
    """Calories burned per km cycling: 70"""
    return distance_km * 70
# main.py

# Import the custom 'fitness_tracker' module
import fitness_tracker

# Ask the user to input the distance they walked, ran, and cycled today
distance_walked = float(input("Enter the distance you walked today (in km): "))
distance_ran = float(input("Enter the distance you ran today (in km): "))
distance_cycled = float(input("Enter the distance you cycled today (in km): "))

# Calculate the total calories burned for each activity
calories_walked = fitness_tracker.walk_calories(distance_walked)
calories_ran = fitness_tracker.run_calories(distance_ran)
calories_cycled = fitness_tracker.cycle_calories(distance_cycled)

# Print the total calories burned for each activity
print(f"Calories burned walking: {calories_walked}")
print(f"Calories burned running: {calories_ran}")
print(f"Calories burned cycling: {calories_cycled}")

# Sum and print the total calories burned for the day
total_calories = calories_walked + calories_ran + calories_cycled
print(f"Total calories burned today: {total_calories}")
#---------------------------------------------------
# Ask the user to input the total loan amount and the monthly repayment amount
loan_amount = float(input("Enter the total loan amount: "))
monthly_payment = float(input("Enter your monthly payment amount: "))

# Use a while loop to simulate the repayment process
while loan_amount > 0:
    loan_amount -= monthly_payment
    if loan_amount < 0:
        loan_amount = 0  # Ensure we don't go into negative loan amount
    print(f"Remaining loan amount: ${loan_amount:.2f}")
    
    # Check if the loan is fully paid off
    if loan_amount == 0:
        print("Congratulations! Your loan is fully paid off.")
        break
