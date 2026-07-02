def perfect_no_check(no):
    lst = []

    for i in range(1, int((no) / 2) + 1):
        if (no % i == 0):
            lst.append(i)

    sum = 0
    for i in lst:
        sum = sum + i
    
    if (sum == no):
        return True
    else:
        return False

def binary_prnt(no):
    ret = ""

    while no > 0:
        ret = str(no % 2) + ret
        no = int(no / 2)

    return ret

def main():
    
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    1. Write a program which accepts length and width of rectangle and prints area.
    '''
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))

    print("Area of the rectangle is: ", length * width)
    #==================================================================================#
    print()
    #==================================================================================#

    '''
    2. Write a program which accepts radius of circle and prints area of circle.
    '''
    radius = float(input("Enter radius of the circle: "))
    PI = 3.14

    print("Area of the circle is: ", PI * (radius * radius))

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    3. Write a program which accepts one number and checks whether it is perfect number or
    not.
    Input: 6
    Output: Perfect Number
    '''
    value = int(input("Enter number: "))

    ret = perfect_no_check(value)

    if (ret == False):
        print(f"{value} is not a Perfect Number")
    else:
        print(f"{value} is a Perfect Number")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    4. Write a program which accepts one number and prints binary equivalent.
    '''
    value = int(input("Enter number: "))

    ret = binary_prnt(value)

    print(f"Binary number for {value} is: {ret}")

    #==================================================================================#
    print()
    #==================================================================================#

    '''
    5. Write a program which accepts marks and displays grade.
    Condition Example:
    • ≥ 75 → Distinction
    • ≥ 60 → First Class
    • ≥ 50 → Second Class
    • < 50 → Fail
    '''
    value = input("Enter your marks: ")

    marks = float(value)

    if marks < 0 or marks > 100:
        print("Invalid entry. Marks must be between 0 and 100.")
    elif marks >= 75:
        print("Grade: Distinction")
    elif marks >= 60:
        print("Grade: First Class")
    elif marks >= 50:
        print("Grade: Second Class")
    else:
        print("Grade: Fail")

    #==================================================================================#
    print()
    #==================================================================================#

if __name__ == "__main__":
    main()