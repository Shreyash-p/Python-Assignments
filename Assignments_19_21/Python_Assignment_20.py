import threading

def evenChk(data):
    lst = []
    for i in data:
        if (i % 2 == 0):
            lst.append(i)

    print(f"First 10 even numbers are: {lst}")
    print()

def oddChk(data):
    lst = []
    for i in data:
        if (i % 2 == 1):
            lst.append(i)

    print(f"First 10 odd numbers are: {lst}")
    print()

def evenFactor(no):
    sum = 0

    for i in range(1, no):
        if (no % i == 0) and (i % 2 == 0):
            sum += i

    print(f"Sum of Even Factors of {no} is: {sum}")
    print()

def oddFactor(no):
    sum = 0

    for i in range(1, no):
        if (no % i == 0) and (i % 2 == 1):
            sum += i

    print(f"Sum of Odd Factors of {no} is: {sum}")
    print()

def evenSum(data):
    sum = 0

    for i in data:
        if (i % 2 == 0):
            sum += i

    print(f"Sum of Even numbers in {data} is: {sum}")
    print()

def oddSum(data):
    sum = 0

    for i in data:
        if (i % 2 == 1):
            sum += i

    print(f"Sum of Odd numbers in {data} is: {sum}")
    print()

def strLowerCaseChk(ipStr):
    print("Thread ID of strLowerCaseChk:", threading.get_ident())
    print("Thread ID of strLowerCaseChk:", threading.current_thread().name)
    new_str = ""

    for i in ipStr:
        if (i.islower()):
            new_str += i
    
    print(f"Lower case characters in {ipStr} are: {new_str}")
    print()

def strUpperCaseChk(ipStr):
    print("Thread ID of strUpperCaseChk:", threading.get_ident())
    print("Thread ID of strUpperCaseChk:", threading.current_thread().name)
    new_str = ""

    for i in ipStr:
        if (i.isupper()):
            new_str += i
    
    print(f"Upper case characters in {ipStr} are: {new_str}")
    print()

def strDigitChk(ipStr):
    print("Thread ID of strDigitChk:", threading.get_ident())
    print("Thread ID of strDigitChk:", threading.current_thread().name)
    new_str = ""

    for i in ipStr:
        if (i.isdigit()):
            new_str += i
    
    print(f"Digit characters in {ipStr} are: {new_str}")
    print()

def Num1To50(data):
    lst = []

    for i in data:
        lst.append(i)

    print(lst)
    print()

def Num50To1(data):
    lst = []

    for i in range(len(data) - 1, -1, -1):
        lst.append(data[i])

    print(lst)
    print()

def main():

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1: Design a Python application that creates two separate threads named Even and Odd.
    • The Even thread should display the first 10 even numbers.
    • The Odd thread should display the first 10 odd numbers.
    • Both threads should execute independently using the threading module.
    • Ensure proper thread creation and execution.
    '''
    lst = list(range(1, 21))
    evenT1 = threading.Thread(target=evenChk, args=(lst,))
    oddT2 = threading.Thread(target=oddChk, args=(lst,))

    evenT1.start()
    evenT1.join()

    oddT2.start()
    oddT2.join()

    
    #==================================================================================#
    print()
    #==================================================================================#
    
    '''
    2: Design a Python application that creates two threads named EvenFactor and OddFactor.
    • Both threads should accept one integer number as a parameter.
    • The EvenFactor thread should:
        ◦ Identify all even factors of the given number.
        ◦ Calculate and display the sum of even factors.
    • The OddFactor thread should:
        ◦ Identify all odd factors of the given number.
        ◦ Calculate and display the sum of odd factors.
    • After both threads complete execution, the main thread should display the message:
    “Exit from main”
    '''
    no = int(input("Enter number: "))
    EvenFactor = threading.Thread(target=evenFactor, args=(no,))
    OddFactor = threading.Thread(target=oddFactor, args=(no,))

    EvenFactor.start()
    EvenFactor.join()

    OddFactor.start()
    OddFactor.join()

    print("Exit from main")
    
    #==================================================================================#
    print()
    #==================================================================================#
    
    '''
    3: Design a Python application that creates two threads named EvenList and OddList.
    • Both threads should accept a list of integers as input.
    • The EvenList thread should:
        ◦ Extract all even elements from the list.
        ◦ Calculate and display their sum.
    • The OddList thread should:
        ◦ Extract all odd elements from the list.
        ◦ Calculate and display their sum.
    • Threads should run concurrently.
    '''
    lst = list(map(int, input("Enter elements of list seperated by ' ': ").split()))

    EvenList = threading.Thread(target=evenSum, args=(lst,))
    OddList = threading.Thread(target=oddSum, args=(lst,))

    EvenList.start()
    EvenList.join()

    OddList.start()
    OddList.join()

    print("Exit from main")
    
    #==================================================================================#
    print()
    #==================================================================================#
    
    '''
    4: Design a Python application that creates three threads named Small, Capital, and Digits.
    • All threads should accept a string as input.
    • The Small thread should count and display the number of lowercase characters.
    • The Capital thread should count and display the number of uppercase characters.
    • The Digits thread should count and display the number of numeric digits.
    • Each thread must also display:
    ◦ Thread ID
    ◦ Thread Name
    '''
    data = input("Enter a string: ")

    small = threading.Thread(target=strLowerCaseChk, args=(data,))
    capital = threading.Thread(target=strUpperCaseChk, args=(data,))
    digits = threading.Thread(target=strDigitChk, args=(data,))
    
    small.start()
    small.join()

    capital.start()
    capital.join()

    digits.start()
    digits.join()

    
    #==================================================================================#
    print()
    #==================================================================================#
    
    '''
    5: Design a Python application that creates two threads named Thread1 and Thread2.
    • Thread1 should display numbers from 1 to 50.
    • Thread2 should display numbers from 50 to 1 in reverse order.
    • Ensure that:
    ◦ Thread2 starts execution only after Thread1 has completed.
    • Use appropriate thread synchronizatio
    '''
    lst = list(range(1, 51))
    Thread1 = threading.Thread(target=Num1To50, args=(lst,))
    Thread2 = threading.Thread(target=Num50To1, args=(lst,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()



    #==================================================================================#
    print()
    #==================================================================================#
    

if __name__ == "__main__":
    main()