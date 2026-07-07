from Arithmetic import *

def Fact(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    
    return fact

def factors(no):
    sum = 0

    for i in range(1, no):
        if (no % i == 0):
            sum += i

    return sum

def prime_check(no):
    flag = True

    if (no <= 1):
        flag = False
    else:
        for i in range(2, no):
            if (no % i == 0):
                flag = False
    return flag

def main():

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
    for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
    parameters as number and perform the operation. Write on python program which call all the
    functions from Arithmetic module by accepting the parameters from user.
    '''

    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))

    print(f"Addition of {val1} and {val2} is: {Add(val1, val2)}")
    print(f"Division of {val1} and {val2} is: {Div(val1, val2)}")
    print(f"Substraction of {val1} and {val2} is: {Sub(val1, val2)}")
    print(f"Multiplication of {val1} and {val2} is: {Mul(val1, val2)}")
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2. Write a program which accept one number and display below pattern.
    Input : 5
    Output : * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    '''
    value = int(input("Enter number: "))

    for i in range(value):
        print(" * " * value)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. Write a program which accept one number from user and return its factorial.
    Input : 5 Output : 120
    '''
    value = int(input("Enter number: "))

    ret = Fact(value)

    print(f"Factorial of {value} is: {ret}")
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4.Write a program which accept one number form user and return addition of its factors.
    Input : 12 Output : 16 (1+2+3+4+6)
    '''
    value = int(input("Enter number: "))

    ret = factors(value)

    print(f"Factors of {value} is: {ret}")
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5.Write a program which accept one number for user and check whether number is prime or not.
    Input : 5 Output : It is Prime Number
    '''
    value = int(input("Enter number: "))

    ret = prime_check(value)

    if (ret == False):
        print(f"{value} is not a Prime Number")
    else:
        print(f"{value} is a Prime Number")
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    6. Write a program which accept one number and display below pattern.
    Input : 5
    Output : * * * * *
    * * * *
    * * *
    * *
    *
    '''
    value = int(input("Enter number: "))

    for i in range(value, 0, -1):
        print(" * " * i)


    #==================================================================================#
    print()
    #==================================================================================#

    '''
    7. Write a program which accept one number and display below pattern.
    Input : 5
    Output : 1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    '''
    value = int(input("Enter number: "))

    for i in range(value):
        row = ""
        for j in range(1, value+1):
            row += str(j) + " "
        print(row)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    8. Write a program which accept one number and display below pattern.
    Input : 5
    Output : 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    '''
    value = int(input("Enter number: "))

    for i in range(1,value+1):
        row = ""
        for j in range(1, i+1):
            row += str(j) + " "
        print(row)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    9. Write a program which accept number from user and return number of digits in that number.
    Input : 5187934 Output : 7
    '''
    value = int(input("Enter number: "))

    print(len(str(value)))
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    10. Write a program which accept number from user and return addition of digits in that number.
    Input : 5187934 Output : 37
    '''
    value = int(input("Enter number: "))

    sum = 0

    for i in range(len(str(value))+1):
        sum += int(i)

    print(sum)

if __name__ == "__main__":
    main()