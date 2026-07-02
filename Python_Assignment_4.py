def Factorial(no):
    sum = 1
    if (no == 1) or (no == 0):
        return sum
    else:
        for i in range(2, no+1):
            sum = (sum * i)
        return sum
    
def multiplication_tbl(no):
    multiplication_str = ""

    for i in range(1, 11):
        multiplication_str = multiplication_str + str(i * no) + " "

    return multiplication_str

def even_no(no):
    even_str = ""
    for i in range(1, no + 1):
        if (i % 2 == 0):
            even_str = even_str + str(i) + " "

    return even_str

def odd_no(no):
    odd_str = ""
    for i in range(1, no + 1):
        if (i % 2 == 1):
            odd_str = odd_str + str(i) + " "

    return odd_str


def main():
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1. Write a program which accepts one number and prints multiplication table of that
    number.
    Input: 4
    Output:
    4 8 12 16 20 24 28 32 36 40
    '''
    value = int(input("Enter number: "))

    multiplication_str = multiplication_tbl(value)

    print(f"Multiplication table of {value} is: {multiplication_str}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2. Write a program which accepts one number and prints sum of first N natural numbers.
    Input: 5
    Output: 15
    '''
    value = int(input("Enter number: "))

    sum = 0
    for i in range(1, value + 1):
        sum += i

    print(f"Sum of first {value} natural numbers is: {sum}")

    #==================================================================================#
    print()
    #==================================================================================#


    '''
    3. Write a program which accepts one number and prints factorial of that number.
    Input: 5
    Output: 120
    '''
    value = int(input("Enter number: "))

    ret = Factorial(value)

    print(f"Factorial of {value} is: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4. Write a program which accepts one number and prints all even numbers till that
    number.
    Input: 10
    Output: 2 4 6 8 10
    '''
    value = int(input("Enter number: "))

    ret = even_no(value)

    print(f"Even numbers till {value} are: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5. Write a program which accepts one number and prints all odd numbers till that number.
    '''
    value = int(input("Enter number: "))

    ret = odd_no(value)

    print(f"Odd numbers till {value} are: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#



if __name__ == "__main__":
    main()

