#Question 1
x = 5
y = 4
x += 3
y *= 2
result = x / y
print("The value of 'result' is:", result)
#---------------------------------------------------------
#Question 2
a = 5
b = 4
c = 3
condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a
final_condition = condition1 or (condition2 and condition3)
print("The value of 'final_condition' is:", final_condition)
#-------------------------------------------------------------
#Question 3
score = int(input("Enter your test score (0-100): "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")
#-----------------------------------------------------------
#Question 4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operation!"
print("The result is:", result)