from functools import reduce

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
    1.Write a program which contains one lambda function which accepts one parameter and return
    power of two.
    Input : 4 Output : 16
    Input : 6 Output : 64
    '''
    value = int(input("Enter number: "))

    print(f"Power of 2 for {value} is: {value**2}")

    #==================================================================================#
    print()
    #==================================================================================#
    '''
    2.Write a program which contains one lambda function which accepts two parameters and return
    its multiplication.
    Input : 4 3 Output : 12
    Input : 6 3 Output : 18
    '''
    mul = lambda a, b : a * b

    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))

    print(f"Multiplication of {val1} and {val2} is: {mul(val1, val2)}")

    #==================================================================================#
    print()
    #==================================================================================#
    '''
    3.Write a program which contains filter(), map() and reduce() in it. 
    Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
    Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
    Map function will increase each number by 10. 
    Reduce will return product of all that numbers.
    Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter = [76, 89, 86, 90, 70]
    List after map = [86, 99, 96, 100, 80]
    Output of reduce = 6538752000
    '''
    greaterThan70 = lambda a : (a >= 70 and a <= 90)
    add10 = lambda a : a + 10
    additionOfAll = lambda a, b : a * b

    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    filtered_lst = list(filter(greaterThan70, lst))
    map_lst = list(map(add10, filtered_lst))
    final_ans = reduce(additionOfAll, map_lst)

    print(f"List after filter: {filtered_lst}")
    print(f"List after map: {map_lst}")
    print(f"Final output: {final_ans}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4.Write a program which contains filter(), map() and reduce() in it. 
    Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
    Filter should filter out all such numbers which are even. Map function will calculate its square.
    Reduce will return addition of all that numbers.
    Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    List after filter = [2, 4, 4, 2, 8, 10]
    List after map = [4, 16, 16, 4, 64, 100]
    Output of reduce = 204
    '''
    evenNo = lambda a : (a % 2 == 0)
    squareCalc = lambda a : a**2
    additionOfAll = lambda a, b : a + b

    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    filtered_lst = list(filter(evenNo, lst))
    map_lst = list(map(squareCalc, filtered_lst))
    final_ans = reduce(additionOfAll, map_lst)

    print(f"List after filter: {filtered_lst}")
    print(f"List after map: {map_lst}")
    print(f"Final output: {final_ans}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5.Write a program which contains filter(), map() and reduce() in it. 
    Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
    Filter should filter out all prime numbers. 
    Map function will multiply each number by 2. 
    Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
    Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
    List after filter = [2, 11, 17, 23, 31]
    List after map = [4, 22, 34, 46, 62]
    Output of reduce = 62
    '''
    primeChk = lambda a : (prime_check(a))
    MulBy2 = lambda a : a * 2
    maxNo = lambda a, b : a if (a > b) else b

    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    filtered_lst = list(filter(primeChk, lst))
    map_lst = list(map(MulBy2, filtered_lst))
    final_ans = reduce(maxNo, map_lst)

    print(f"List after filter: {filtered_lst}")
    print(f"List after map: {map_lst}")
    print(f"Final output: {final_ans}")

if __name__ == "__main__":
    main()