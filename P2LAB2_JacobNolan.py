# Nolan Jacob
# 10/2/24
# P2LAB2
# Using Dictionaries

# Make dctionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

#print all keys in dictionary
print(cars.keys)
print()

# user chooses a car type
user_choice = input("Enter a vehicle to see it's mpg: ")
print()

#display MPG for user choice
print(f"The {user_choice} gets {cars[user_choice]} mpg.")
print()

#user inputs distance
distance = int(input(f"How many miles will you drive the {user_choice}?"))
print()

# Calculate the amount of gas needed to drive the inputed distance
gas_needed = distance / cars[user_choice]
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {user_choice} {distance} miles.")
