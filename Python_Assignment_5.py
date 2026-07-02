def prime_check(no):
    flag = True

    if (no <= 1):
        flag = False
    else:
        for i in range(2, no):
            if (no % i == 0):
                flag = False
    return flag

def no_count(no):
    no = str(no)
    ctr = 0
    for i in no:
        ctr = ctr + 1

    return ctr

def digit_sum(no):
    no = str(no)
    sum = 0
    for i in no:
        sum = sum + int(i)

    return sum

def rev_no(no):
    no = str(no)[::-1]
    return no

def palindrome_check(no):
    rev_no = str(no)[::-1]
    return no == int(rev_no)

def main():
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1. Write a program which accepts one number and checks whether it is prime or not.
    Input: 11
    Output: Prime Number
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
    2. Write a program which accepts one number and prints count of digits in that number.
    Input: 7521
    Output: 4
    '''
    value = int(input("Enter number: "))

    ret = no_count(value)

    print(f"Number count in {value} is: {ret}")
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. Write a program which accepts one number and prints sum of digits.
    Input: 123
    Output: 6
    '''
    value = int(input("Enter number: "))

    ret = digit_sum(value)

    print(f"Sum of number in {value} is: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4. Write a program which accepts one number and prints reverse of that number.
    Input: 123
    Output: 321
    '''
    value = int(input("Enter number: "))

    ret = rev_no(value)

    print(f"Reverse of number in {value} is: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5. Write a program which accepts one number and checks whether it is palindrome or not.
    Input: 121
    Output: Palindrome
    '''
    value = int(input("Enter number: "))

    ret = palindrome_check(value)

    if (ret == False):
        print(f"{value} is not a Palindrome")
    else:
        print(f"{value} is a Palindrome")

    #==================================================================================#
    print()
    #==================================================================================#
    

if __name__ == "__main__":
    main()