def vowel_check(ip_char):
    vowel_lst = ["A", "E", "I", "O", "U"]

    if (ip_char.upper() not in vowel_lst):
        return False
    else:
        return True

def factors_check(no):
    ret_lst = ""
    for i in range(1, no):
        if (no % i == 0):
            ret_lst = ret_lst + str(i) + " "
            
    return ret_lst

def print_num(no):
    ret = ""

    for i in range(1, no + 1):
        ret = ret + str(i) + " "

    return ret.strip()

def main():
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1. Write a program which accepts one character and checks whether it is vowel or
    consonant.
    Input: a
    Output: Vowel
    '''
    value = input("Enter a chracter: ")

    ret = vowel_check(value)

    if (ret == False):
        print(f"{value} is a consonant")
    else:
        print(f"{value} is a Vowel")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2. Write a program which accepts one number and prints its factors.
    Input: 12
    Output: 1 2 3 4 6 12
    '''
    value = int(input("Enter number: "))

    ret = factors_check(value)

    print(f"Factors of {value} are: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. Write a program which accepts two numbers and prints addition, subtraction,
    multiplication and division.
    '''
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))

    print("Addition is:", value1 + value2)
    print("Subtraction is:", value1 - value2)
    print("multiplication is:", value1 * value2)
    print("Division is:", value1 / value2)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4. Write a program which accepts one number and prints that many numbers starting
    from 1.
    Input: 5
    Output: 1 2 3 4 5
    '''
    value = int(input("Enter number: "))

    ret = print_num(value)

    print(ret)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5. Write a program which accepts one number and prints that many numbers in reverse
    order.
    Input: 5
    Output: 5 4 3 2 1
    '''

    value = int(input("Enter number: "))

    ret = print_num(value)

    print(ret[::-1])

    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()