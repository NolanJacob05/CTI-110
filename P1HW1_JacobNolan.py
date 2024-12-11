# Nolan Jacob
# 9/16/24
# P1HW1
# using math expressions with user input

print("-----Calculating Exponenets-----")
print()
print()
# user inputs base value integer
base = int(input("Enter an integer as the base value: "))
# user inputs exponenet integer
exponenet = int(input("Enter an integer as the exponenet: "))
print()
#display result to the user
print(base, "raised to the power of ",exponenet, "is ", str(base**exponenet) + "!!")
print()

print()


print("-----Addition and Subtraction-----")
print()
print()

#get integers from user
start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))
print()
print()

#Calculate Equation
end_num = start_num + add_num - sub_num

#Disply result to user
print(start_num, "+", add_num, "-", sub_num, "is equal to", end_num)
