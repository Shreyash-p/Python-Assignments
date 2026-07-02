from functools import reduce

def main():

    lst = list(map(int, input("Enter a list of numbers seperated by ' ' : ").split()))
    lst_str = list(map(str, input("Enter a list of strings seperated by ' ' : ").split()))

    #==================================================================================#
    print()
    #==================================================================================#

    '''1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.'''
    square = lambda a : a * a

    print(f"Square of {lst} is:", list(map(square, lst)))

    #==================================================================================#
    print()
    #==================================================================================#

    '''2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.'''
    even = lambda a : a % 2 == 0

    print(f"Even numbers in given list {lst} are:", list(filter(even, lst)))

    #==================================================================================#
    print()
    #==================================================================================#

    '''3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.'''
    odd = lambda a : a % 2 == 1

    print(f"Odd numbers in given list {lst} are:", list(filter(odd, lst)))

    #==================================================================================#
    print()
    #==================================================================================#

    '''4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.'''
    add = lambda a, b : a + b

    print(f"Addition of all elements in {lst} is:", reduce(add, lst))

    #==================================================================================#
    print()
    #==================================================================================#

    '''5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.'''
    max = lambda a, b : a if a > b else b

    print(f"Maximun number of all elements in {lst} is:", reduce(max, lst))

    #==================================================================================#
    print()
    #==================================================================================#

    '''6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.'''
    min = lambda a, b : a if a < b else b

    print(f"Minimum number of all elements in {lst} is:", reduce(min, lst))

    #==================================================================================#
    print()
    #==================================================================================#

    length_more_than_5 = lambda a : a if len(a) > 5 else None

    print(f"String having length more than 5 in {lst_str} are:", list(filter(length_more_than_5, lst_str)))

    #==================================================================================#
    print()
    #==================================================================================#

    '''8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.'''
    divisible_by_3_5 = lambda a : (a % 3 == 0 and a % 5 == 0)

    print(f"Numbers divisible by 3 & 5 in given list {lst} are:", list(filter(divisible_by_3_5, lst)))

    #==================================================================================#
    print()
    #==================================================================================#

    '''9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.'''
    product = lambda a, b : a * b

    print(f"Product of all elements in {lst} is:", reduce(product, lst))

    #==================================================================================#
    print()
    #==================================================================================#

    '''10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.'''
    even_cnt = lambda a : 1 if (a % 2 == 0) else 0

    print(f"Total even numbers in given list {lst} is:", len(list(filter(even_cnt, lst))))

    #==================================================================================#
    print()
    #==================================================================================#


if __name__ == "__main__":
    main()