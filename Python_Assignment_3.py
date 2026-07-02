def Display():
    print("Jay Ganesh.")

def ChkGreater(no1, no2):
    flag = 0
    if (no1 > no2):
        flag = 1
    elif (no2 > no1):
        flag = 2
    
    return flag


def main():
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1. Write a program which contains one function named as Display() that prints "Jay
    Ganesh" on console.
    '''
    Display()

    #==================================================================================#
    print()
    #==================================================================================#
    
    '''
    2. Write a program which contains one function ChkGreater() that accepts two numbers
    and prints the greater number.
    Input: 10 20
    Output: 20 is greater
    '''
    no1, no2 = map(int, input("Enter both number: ").split())

    ret = ChkGreater(no1, no2)
    if (ret == 0):
        print("Both numbers are same")
    elif (ret == 1):
        print(f"{no1} is greater")
    else:
        print(f"{no2} is greater")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. Write a program which accepts one number and prints square of that number.
    Input: 5
    Output: 25
    '''
    value = int(input("Enter number: "))
    print(f"Square of {value} is: {value * value}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4. Write a program which accepts one number and prints cube of that number.
    '''
    value = int(input("Enter number: "))
    print(f"Cube of {value} is: {value * value * value}")
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
    Input: 15
    Output: Divisible by 3 and 5
    '''
    value = int(input("Enter number: "))

    if (value % 3 == 0) and (value % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("NOT Divisible by 3 and 5")
    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()
