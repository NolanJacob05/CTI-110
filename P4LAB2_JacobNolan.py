# Nolan Jacob
# 10/30/24
# P4LAB2
# using loops for multiplication 

# while loop to control program
run_again = "yes"


while run_again == "yes":

# get integer from user
    user_int = int(input("Enter an integer: "))
    
# if input is positive
    if user_int >= 0:
        print()
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int * num}")

# if input is negative
    else:
        print()
        print("Program does not manage negative numbers")
    
    print()
    run_again = input("Would you like to run the program again?(yes/no) ").lower()
    print()

# loop breaks
print("Exiting Program")
print()
