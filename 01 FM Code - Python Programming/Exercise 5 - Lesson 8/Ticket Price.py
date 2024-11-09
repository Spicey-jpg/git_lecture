# Define ticket price
ticket_price = 10.0  # Example price per ticket

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask the user for the number of tickets they want to buy
num_tickets = int(input("Enter the number of tickets you want to buy: "))

# Ask the user if they have a discount (yes/no)
has_discount = input("Do you have a discount? (yes/no): ").lower() == 'yes'

# Calculate discount eligibility
if has_discount:
    discount_rate = 0.2  # Example discount rate of 20%
else:
    discount_rate = 0.0

# Calculate the total price
total_price = num_tickets * ticket_price * (1 - discount_rate)

# Ask the user if they have enough money
money_available = float(input("Enter the amount of money you have: "))

# Check if they have enough money
if money_available >= total_price:
    print(f"You can buy the tickets! Your total is: R{total_price:.2f}")
else:
    print(f"Sorry, you need R{(total_price - money_available):.2f} more to buy the tickets.")

# Print the result
print(f"Total price: R{total_price:.2f}")
print(f"Money available: R{money_available:.2f}")
