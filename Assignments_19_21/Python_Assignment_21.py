import threading

shared_val = 1

def prime_check(data):
    lst = []

    for no in data:
        flag = True
        if (no <= 1):
            flag = False
        else:
            for i in range(2, no):
                if (no % i == 0):
                    flag = False

        if flag == True:
            lst.append(no)

    print(f"Prime numbers present in {data} are: \n{lst}")
    print()

def non_prime_check(data):
    lst = []

    for no in data:
        flag = False
        if (no <= 1):
            flag = True
        else:
            for i in range(2, no):
                if (no % i == 0):
                    flag = True

        if flag == True:
            lst.append(no)

    print(f"Non Prime numbers present in {data} are: \n{lst}")
    print()

def max_no(data):
    max_no = data[0]

    for i in data:
        if (max_no<i):
            max_no = i
    
    print(f"Maximum number in {data} is: {max_no}")
    print()

def min_no(data):
    min_no = data[0]

    for i in data:
        if (min_no>i):
            min_no = i
    
    print(f"Minimum number in {data} is: {min_no}")
    print()

def update_counter(incr_val, lock, thread_name):
    global shared_val

    print(f"Thread name: {thread_name}")
    print(f"Current value of shared value is: {shared_val}")

    with lock:
        shared_val = shared_val + incr_val

    print(f"New Shared value is: {shared_val}")

def sum_of_lst(data, thread_name, output):
    sum = 0

    for i in data:
        sum += i

    output[thread_name] = sum

def product_of_lst(data, thread_name, output):
    product = 1

    for i in data:
        product *= i

    output[thread_name] = product

def main():

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1: Design a Python application that creates two threads named Prime and NonPrime.
    • Both threads should accept a list of integers.
    • The Prime thread should display all prime numbers from the list.
    • The NonPrime thread should display all non-prime numbers from the list.
    '''
    lst = list(range(1, 40))

    Prime = threading.Thread(target=prime_check, args=(lst,))
    NonPrime = threading.Thread(target=non_prime_check, args=(lst,))

    Prime.start()
    Prime.join()

    NonPrime.start()
    NonPrime.join()


    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2: Design a Python application that creates two threads.
    • Thread 1 should calculate and display the maximum element from an list.
    • Thread 2 should calculate and display the minimum element from the same list.
    • The list should be accepted from the user.
    '''
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    t1 = threading.Thread(target=max_no, args=(lst,))
    t2 = threading.Thread(target=min_no, args=(lst,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3: Design a Python application where multiple threads update a shared variable.
    • Use a Lock to avoid race conditions.
    • Each thread should increment the shared counter multiple times.
    • Display the final value of the counter after all threads complete execution.
    '''
    increment_val = 1

    lock = threading.Lock()

    t1 = threading.Thread(target=update_counter, args=(increment_val, lock, "Thread - A",))
    t2 = threading.Thread(target=update_counter, args=(increment_val, lock,"Thread - B",))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4: Design a Python application that creates two threads.
    • Thread 1 should compute the sum of elements from a list.
    • Thread 2 should compute the product of elements from the same list.
    • Return the results to the main thread and display them.
    '''
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))
    output = {}

    t1 = threading.Thread(target=sum_of_lst, args=(lst, "Thread 1", output,))
    t2 = threading.Thread(target=product_of_lst, args=(lst, "Thread 2", output,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print(f"Sum of all elements of {lst} is: {output['Thread 1']}")
    print(f"Product of all elements of {lst} is: {output['Thread 2']}")

    #==================================================================================#
    print()
    #==================================================================================#


if __name__ == "__main__":
    main()