import multiprocessing
import os
import time

def squareSum(data):
    sum = 0

    for i in range(1, data+1):
        sum = sum + (i * i)

    return sum

def factorial(no):
    print("Process is running with PID:", os.getpid())

    fact = 1
    
    for i in range(1, no+1):
        fact *= i

    return fact

def primeNo(no):
    ret = []
    
    for i in range(2, no):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            ret.append(i)

    return ret

def Penteract(no):
    sum = 0

    for i in range(1, no+1):
        sum = sum + (i**5)

    return sum

def main():

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.
    Example Input
    [1000000,2000000,3000000,4000000]
    Expected Output
    [333333833333500000,2666668666667000000,...]
    '''
    lst = [1000000,2000000,3000000,4000000]
    result = []

    pobj = multiprocessing.Pool()

    result = pobj.map(squareSum, lst)

    pobj.close()
    pobj.join()

    print(f"Sum of squares of {lst} from 1 to N is: ")
    print(result)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
    Input
    [10,15,20,25]
    Display
    • Process ID
    • Input Number
    • Factorial
    '''
    lst = [10,15,20,25]
    result = []

    pobj = multiprocessing.Pool()

    result = pobj.map(factorial, lst)

    pobj.close()
    pobj.join()

    print(f"factorials of {lst} are: ")
    print(result)

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
    Example
    10000
    20000
    30000
    40000
    Display total prime count for each number.
    '''
    lst = [10000, 20000, 30000, 40000]
    result = []

    pobj = multiprocessing.Pool()

    result = pobj.map(primeNo, lst)

    pobj.close()
    pobj.join()

    print(f"Prime numbers in {lst} are: ")
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4. Write a program that calculates 
    1^5+2^5+3^5+.....+N^5
    for multiple values of N simultaneously using Pool.
    Input

    [1000000,
    2000000,
    3000000,
    4000000]
    Measure total execution time.`
    '''
    lst = [1000000, 2000000, 3000000, 4000000]
    result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    result = pobj.map(Penteract, lst)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Sum of Penteract of {lst} from 1 to N is: ")
    print(result)
    print(f"Time required: {end_time-start_time:.4f} seconds")

    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()