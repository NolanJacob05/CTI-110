# Nolan Jacob
# 9/25/24
# P1HW2
# Calculate budget for a trip

print("This program calculates and displays travel expences")
print()
print()

# get user to enter budget
budget = int(input("Enter the budget for your trip: "))
print()


# get where user is traveling
destination = input("Enter your travel destination: ")
print()
# user input amount of gas money
gas_price = int(input("How much do you expect to spend on gas? "))
print()
# user inputs amount for accomidation
accomodation_price = int(input("About how much will you need for accomodation? "))
print()
# user inputs amount for food
food_price = int(input("Lastly, Hw much do you need for food? "))
print()
print()

print("----------Travel Expenses----------")

# shows amount spent on each expense
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()

print(f"Fuel: {gas_price}")
print(f"Accomodation: {accomodation_price}")
print(f"Food: {food_price}")
print()

# add expenses and substract from budget
total_expense = gas_price + accomodation_price + food_price
remaining_budget = budget - total_expense
print(f"Remaining Balance: {remaining_budget}")
