def pizza_calculator(guests, slices_per_person):
    """Calculates the total number of pizza slices needed."""
    return guests * slices_per_person

guests = int(input("How many guests are you inviting? "))

slices_per_person = int(input("How many slices will each person eat? "))

total_slices = pizza_calculator(guests, slices_per_person)

print(f"You will need {total_slices} slices of pizza.")