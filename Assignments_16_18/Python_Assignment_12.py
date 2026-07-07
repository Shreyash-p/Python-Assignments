from functools import reduce
from MarvellousNum import ChkPrime

def lstAddition(lst):
    sum = 0

    for i in lst:
        sum =+ i

    return sum

def lstMaxNo(lst):
    max_ele = lst[0]

    for i in range(1, len(lst)):
        if (lst[i] > max_ele):
            max_ele = lst[i]
        
    return max_ele

def lstMinNo(lst):
    min_ele = lst[0]

    for i in range(1, len(lst)):
        if (lst[i] < min_ele):
            min_ele = lst[i]
        
    return min_ele
        
def lstSearch(lst, ele_to_srch):
    max = lambda a, b : a if a > b else b

    d = {}

    for i in lst:
        d[i] = d.get(i, 0) + 1

    ret = reduce(max, list(d.values()))
    
    return ret

def ListPrime(lst):
    prime_no = []
    sum = 0

    for i in lst:
        ret = ChkPrime(i)

        if (ret == True):
            sum += i
        
    return sum


def main():
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1.Write a program which accept N numbers from user and store it into List. Return addition of all
    elements from that List.
    Input : Number of elements : 6
    Input Elements : 13 5 45 7 4 56
    Output : 130
    '''
    lst_len = int(input("Enter the number of elements in list: "))
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    #print(f"Addition of {lst} elements is: {lstAddition(lst)}")

    #==================================================================================#
    print()
    #==================================================================================#
    '''
    2.Write a program which accept N numbers from user and store it into List. Return Maximum
    number from that List.
    Input : Number of elements : 7
    Input Elements : 13 5 45 7 4 56 34
    Output : 56 
    '''
    lst_len = int(input("Enter the number of elements in list: "))
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    #print(f"Max elements of {lst} is: {lstMaxNo(lst)}")

    #==================================================================================#
    print()
    #==================================================================================#
    '''
    3.Write a program which accept N numbers from user and store it into List. Return Minimum
    number from that List.
    Input : Number of elements : 4
    Input Elements : 13 5 45 7
    Output : 5
    '''
    lst_len = int(input("Enter the number of elements in list: "))
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    print(f"Min elements of {lst} is: {lstMinNo(lst)}")

    #==================================================================================#
    print()
    #==================================================================================#
    '''
    4.Write a program which accept N numbers from user and store it into List. Accept one another
    number from user and return frequency of that number from List.
    Input : Number of elements : 11
    Input Elements : 13 5 45 7 4 56 5 34 2 5 65
    Element to search : 5
    Output : 3
    '''
    lst_len = int(input("Enter the number of elements in list: "))
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))
    ele_to_src = int(input("Enter the number of you want to search: "))

    print(f"Count of {ele_to_src} in {lst} is: {lstSearch(lst, ele_to_src)}")

    #==================================================================================#
    print()
    #==================================================================================#
    '''
    5.Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
    Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
    Name of the function from main python file should be ListPrime().
    Input : Number of elements : 11
    Input Elements : 13 5 45 7 4 56 10 34 2 5 8
    Output : 32 (13 + 5 + 7 +2 + 5)
    '''
    lst_len = int(input("Enter the number of elements in list: "))
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    print(f"Addition of all prime numbers present in {lst} is: {ListPrime(lst)}")

    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()