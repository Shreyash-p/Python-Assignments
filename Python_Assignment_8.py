def main():

    no1 = int(input("Enter 1st Number: "))
    no2 = int(input("Enter 2nd Number: "))
    no3 = int(input("Enter 3rd Number: "))

    #==================================================================================#
    print()
    #==================================================================================#

    '''1. Write a lambda function which accepts one number and returns square of that number.'''
    square = lambda a : a * a

    print(f"Square of {no1} is:", square(no1))

    #==================================================================================#
    print()
    #==================================================================================#

    '''2. Write a lambda function which accepts one number and returns cube of that number.'''
    cube = lambda a : a * a * a

    print(f"Cube of {no1} is:", cube(no1))

    #==================================================================================#
    print()
    #==================================================================================#

    '''3. Write a lambda function which accepts two numbers and returns maximum number.'''
    max_no = lambda a, b : max(a, b)

    print(f"Max number between {no1} and {no2} is:", max_no(no1, no2))

    #==================================================================================#
    print()
    #==================================================================================#

    '''4. Write a lambda function which accepts two numbers and returns minimum number.'''
    min_no = lambda a, b : min(a, b)

    print(f"Min number between {no1} and {no2} is:", min_no(no1, no2))

    #==================================================================================#
    print()
    #==================================================================================#

    '''5. Write a lambda function which accepts one number and returns True if number is even otherwise False.'''
    even = lambda a : a % 2 == 0

    print(f"Number {no1} is Even:", even(no1))

    #==================================================================================#
    print()
    #==================================================================================#

    '''6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.'''
    odd = lambda a : a % 2 == 1

    print(f"Number {no1} is Odd:", odd(no1))

    #==================================================================================#
    print()
    #==================================================================================#

    '''7. Write a lambda function which accepts one number and returns True if divisible by 5.'''
    divisible_by_5 = lambda a : a % 5 == 0

    print(f"Number {no1} is divisible by 5:", divisible_by_5(no1))

    #==================================================================================#
    print()
    #==================================================================================#

    '''8. Write a lambda function which accepts two numbers and returns addition.'''
    add = lambda a, b : a + b

    print(f"Addition of {no1} and {no2} is:", add(no1, no2))

    #==================================================================================#
    print()
    #==================================================================================#

    '''9. Write a lambda function which accepts two numbers and returns multiplication.'''
    mull = lambda a, b : a * b

    print(f"Addition of {no1} and {no2} is:", mull(no1, no2))

    #==================================================================================#
    print()
    #==================================================================================#

    '''10. Write a lambda function which accepts three numbers and returns largest number.'''
    largest_of_three = lambda a, b, c : max(a, b, c)

    print(f"Max number between {no1}, {no2} and {no3} is:", largest_of_three(no1, no2, no3))

    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()