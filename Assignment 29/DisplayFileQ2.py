import sys
import os

def main():

    '''
    Q2) Display File Contents
    Problem Statement:
    Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
    Input:
    Demo.txt
    Expected Output:
    Display contents of Demo.txt on console.
    '''
    fileName = sys.argv[1]

    try:
        fobj = open(fileName, "r")

        print(fobj.read())

        fobj.close()
    
    except FileNotFoundError as fe:
        print("File not found")


if __name__ == "__main__":
    main()