# Nolan Jacob
# 11/13/24
# P5LAB
# Calculating most efficient way to sort change using functions

#Import random library to use in function
import random



def disperse_change(change):
    # find the ammount of dollars
    change = round(change * 100)
    dollars = change // 100
    dollars = int(dollars)
    if dollars > 1:
        print(f"{dollars} Dollars")
    elif dollars == 1:
        print(f"{dollars} Dollar")
    else:
        pass

    # Find ammount of quarters
    coins = change % 100
    quarters = coins // 25
    quarters = int(quarters)
    if quarters > 1:
        print(f"{quarters} Quarters")
    elif quarters == 1:
        print(f"{quarters} Quarter")
    else:
        pass

    #Find ammount of dimes
    coins = coins - quarters * 25
    dimes = coins // 10
    dimes = int(dimes)
    if dimes > 1:
        print(f"{dimes} Dimes")
    elif dimes == 1:
        print(f"{dimes} Dime")
    else:
        pass

    # Find ammount of nickels
    coins = coins - dimes * 10
    nickels = coins // 5
    nickels = int(nickels)
    if nickels > 1:
        print(f"{nickels} Nickels")
    elif nickels == 1:
        print(f"{nickels} Nickel")
    else:
        pass

    # Find ammount of pennies
    coins = coins - nickels * 5
    pennies = coins // 1
    pennies = int(pennies)
    if pennies > 1:
        print(f"{pennies} Pennies")
    elif pennies == 1:
        print(f"{pennies} Penny")
    else:
        pass

    # display no change if 0 dollars is entered
    if dollars < 1 and quarters < 1 and dimes < 1 and nickels < 1 and pennies < 1:
        print("No Change")
    else:
        pass


# Define the main function
def main():
    print("Welcome to the store!")
    print()
    #Generate money owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")
    user_amount = float(input("How much cash will you put in the self-checkout? $"))
    change = user_amount - amount_owed
    change = round(change, 2)
    print(f"Change is: ${change:.2f}")

    #Call the disperse_change function
    disperse_change(change)

# Call the main
if __name__ == "__main__":
    main()
