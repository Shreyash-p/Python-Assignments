def Fun():
    print("Hello from Fun")

def ChkNum(no):
    if (no % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def Add(no1, no2):
    return no1 + no2

def ChkPosNev(no):
    if (no < 0):
        print("Negative number")
    elif (no == 0):
        print("Zero")
    else:
        print("Positive Number")

def divisibleBy5(no):
    if (no % 5 == 0):
        print("True")
    else:
        print("False")

def str_len(ip):
    print(len(ip))

def main():

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1.Write a program which contains one function named as Fun(). That function should display
    “Hello from Fun” on console.
    '''
    Fun()

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2. Write a program which contains one function named as ChkNum() which accept one
    parameter as number. If number is even then it should display “Even number” otherwise
    display “Odd number” on console.
    Input : 11 Output : Odd Number
    Input : 8 Output : Even Number
    '''
    value = int(input("Enter number: "))

    ChkNum(value)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. Write a program which contains one function named as Add() which accepts two numbers
    from user and return addition of that two numbers.
    Input : 11 5 Output : 16
    '''
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    ret = Add(value1, value2)

    print(f"Addition of {value1} and {value2} is: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4.Write a program which display 5 times Marvellous on screen.
    Output : Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    '''
    print(f"Marvellous\n" * 5)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5.Write a program which display 10 to 1 on screen.
    Output : 10 9 8 7 6 5 4 3 2 1
    '''
    lst = []

    for i in range(10, 0, -1):
        lst.append(i)

    print(lst)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    6.Write a program which accept number from user and check whether that number is positive or
    negative or zero.
    Input : 11 Output : Positive Number
    Input : -8 Output : Negative Number
    Input : 0 Output : Zero
    '''
    value = int(input("Enter number: "))

    ChkPosNev(value)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    7. Write a program which contains one function that accept one number from user and returns
    true if number is divisible by 5 otherwise return false.
    Input : 8 Output : False
    Input : 25 Output : True
    '''
    value = int(input("Enter number: "))

    divisibleBy5(value)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    8. Write a program which accept number from user and print that number of “*” on screen.
    Input : 5 Output : * * * * *
    '''
    value = int(input("Enter number: "))

    print("*" * value)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    9. Write a program which display first 10 even numbers on screen.
    Output : 2 4 6 8 10 12 14 16 18 20
    '''
    lst = []

    for i in range(2, 20, 2):
        lst.append(i)

    print(lst)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    10. Write a program which accept name from user and display length of its name.
    Input : Marvellous Output : 10
    '''

    ip_str = input("Enter a string: ")

    str_len(ip_str)





if __name__ == "__main__":
    main()