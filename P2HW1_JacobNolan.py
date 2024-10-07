# Nolan Jacob
# 9/25/24
# P2HW1
# Calculate budget for a trip

print("This program calculates and displays travel expences")
print()
print()

# get user to enter budget
budget = float(input("Enter the budget for your trip: "))
print()


# get where user is traveling
destination = input("Enter your travel destination: ")
print()
# user input amount of gas money
gas_price = float(input("How much do you expect to spend on gas? "))
print()
# user inputs amount for accomidation
accomodation_price = float(input("About how much will you need for accomodation? "))
print()
# user inputs amount for food
food_price = float(input("Lastly, How much do you need for food? "))
print()
print()

print("----------Travel Expenses----------")

# shows amount spent on each expense
print(f"{'Location:':<20}{destination:<20}")
print(f"{'Initial Budget:':<20}${budget:<20.2f}")
print(f"{'Fuel:':<20}${gas_price:<20.2f}")
print(f"{'Accomodation:':<20}${accomodation_price:<20.2f}")
print(f"{'Food:':<20}${food_price:<20.2f}")
print("--" *18)
print()
# add expenses and substract from budget
total_expense = gas_price + accomodation_price + food_price
remaining_budget = budget - total_expense
print(f"{'Remaining Balance:':<20}${remaining_budget:<20.2f}")
