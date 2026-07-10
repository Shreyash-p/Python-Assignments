import multiprocessing
import os

def sumEven(no):
    sum = 0

    for i in range(2, no+1, 2):
        sum += i

    return {"pid" : os.getpid(), "input" : no, "sum" : sum}

def sumOdd(no):
    sum = 0

    for i in range(1, no+1, 2):
        sum += i

    return {"pid" : os.getpid(), "input" : no, "sum" : sum}

def evenCnt(no):
    ctr = 0

    for i in range(2, no+1, 2):
        ctr += 1

    return {"pid" : os.getpid(), "input" : no, "count" : ctr}

def oddCnt(no):
    ctr = 0

    for i in range(1, no+1, 2):
        ctr += 1

    return {"pid" : os.getpid(), "input" : no, "count" : ctr}

def factorial(no):

    fact = 1
    
    for i in range(1, no+1):
        fact *= i

    return {"pid" : os.getpid(), "input" : no, "Factorial" : fact}

def main():
    '''
    1: Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.
    Input
    Data = [1000000, 2000000, 3000000, 4000000]
    Expected Task
    For each number N, calculate:
    2 + 4 + 6 + ... + N
    Expected Output Format
    Process ID : 1234
    Input Number : 1000000
    Sum of Even Numbers : 250000500000
    '''
    data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    ret = pobj.map(sumEven, data)

    pobj.close()
    pobj.join()

    for res in ret:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Sum of Even Numbers : {res['sum']}")
        print("-" * 35) 

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2: Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.
    Input
    Data = [1000000, 2000000, 3000000, 4000000]
    Expected Task
    For each number N, calculate:

    1 + 3 + 5 + ... + N
    Expected Output Format

    Process ID : 1235
    Input Number : 1000000
    Sum of Odd Numbers : 250000000000
    '''
    data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    ret = pobj.map(sumOdd, data)

    pobj.close()
    pobj.join()

    for res in ret:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Sum of Odd Numbers : {res['sum']}")
        print("-" * 35) 

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3: Write a program that counts how many even numbers exist between 1 and N using Pool.map().
    Input
    Data = [1000000, 2000000, 3000000, 4000000]
    Expected Output Format
    Process ID : 1236
    Input Number : 1000000
    Even Number Count : 500000
    '''
    data = [1000000, 2000000, 3000000, 4000000]

    with multiprocessing.Pool() as pool:
        ret = pool.map(evenCnt, data)

    for res in ret:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Even Number Count : {res['count']}")
        print("-" * 35) 

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4: Write a program that counts how many odd numbers exist between 1 and N.
    Input
    Data = [1000000, 2000000, 3000000, 4000000]
    Expected Output Format
    Process ID : 1237
    Input Number : 1000000
    Odd Number Count : 500000
    '''
    data = [1000000, 2000000, 3000000, 4000000]

    with multiprocessing.Pool() as pool:
        ret = pool.map(oddCnt, data)

    for res in ret:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Odd Number Count : {res['count']}")
        print("-" * 35) 

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5: Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
    Input

    Data = [10, 15, 20, 25]
    Expected Task
    For every N, calculate: N!
    Expected Output Format
    Process ID : 1240
    Input Number : 20
    Factorial : 2432902008176640000
    '''
    data = [10, 15, 20, 25]
    result = []

    pobj = multiprocessing.Pool()

    result = pobj.map(factorial, data)

    pobj.close()
    pobj.join()

    for res in result:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Factorial : {res['Factorial']}")
        print("-" * 35) 

    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()