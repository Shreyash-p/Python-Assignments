import sys

'''
1.Write a program to display:
• Value
• Type
• Memory address
for a variable using appropriate built-in functions.
'''
a=10

print("Value:", a)
print("Type:", type(a))
print("getsizeof:", sys.getsizeof(a))

####################################################################################################
####################################################################################################

'''
6. Write a program that accepts two numbers from user and prints their:
• Addition
• Subtraction
• Multiplication
• Division
'''
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
####################################################################################################
####################################################################################################

'''
9. Write a program to take user’s name and age and display:
Hello <name>, you will turn <age+1> next year.
'''
name=input("Enter your name: ")
age=int(input("Enter your age: "))

print(f"Hello {name}, you will turn {age+1} next year.")
####################################################################################################
####################################################################################################
