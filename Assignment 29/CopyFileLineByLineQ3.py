import sys
import os

def main():

    '''
    Q3) Copy File Contents into a New File (Command Line)
    Problem Statement:
    Write a program which accepts an existing file name through command line arguments, creates a new file
    named Demo.txt, and copies all contents from the given file into Demo.txt.
    Input (Command Line):
    ABC.txt
    Expected Output:
    Create Demo.txt and copy contents of ABC.txt into Demo.txt.
    '''
    fileName1 = sys.argv[1]
    fileName2 = "Demo1.txt"

    try:
        fobj1 = open(fileName1, "r")
        fobj2 = open(fileName2, "w")

        for line in fobj1:
            fobj2.write(line)

        fobj1.close()
        fobj2.close()
    
    except FileNotFoundError as fe:
        print("File not found")


if __name__ == "__main__":
    main()