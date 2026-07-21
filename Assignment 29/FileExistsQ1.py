import sys
import os

def main():

    '''
    Q1) Check File Exists in Current Directory
    Problem Statement:
    Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not. 
    Input:
    Demo.txt
    Expected Output:
    Display whether Demo.txt exists or not.
    '''
    fileName = sys.argv[1]

    if (os.path.exists(fileName)):
        print(f"File {fileName} exists in current directory")


if __name__ == "__main__":
    main()