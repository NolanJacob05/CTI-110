# learning to use user defined functions

# Define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)

#define an add function
def add(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)

def return_num():
    user_input = input("Give me a big number: ")
    while not user_input.isnumeric():
        print("value must be a number")
        user_input = input("Give me a big number: ")
    return int(user_input)


def get_name(lastname):
    name = input("Enter your first name: ")
    fullname = "**********" + name + "**********" + lastname
    return fullname


#define the main function - all your logic goes here
def main():
    # Get input from user
    first_num = int(input("input number: "))
    second_num = int(input("input number: "))
    third_num = int(input("input number: "))
    
    # Call the multiply function
    multiply(first_num, second_num, third_num)

    #Call the add function
    add(first_num, second_num, third_num)

    # Call the value returning function
    big_num = return_num()

    print(big_num * 5)

    print(get_name("Jacob"))

#Call the main function
if __name__ == "__main__":
    main()