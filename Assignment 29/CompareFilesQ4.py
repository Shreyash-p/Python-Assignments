import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def main():

    '''
    Q4) Compare Two Files (Command Line)
    Problem Statement:
    Write a program which accepts two file names through command line arguments and compares the contents of both files.
    • If both files contain the same contents, display Success
    • Otherwise display Failure
    Input (Command Line):
    Demo.txt Hello.txt
    Expected Output:
    Success OR Failure
    '''
    fileName1 = sys.argv[1]
    fileName2 = sys.argv[2]


    ret1 = CalculateCheckSum(fileName1)
    ret2 = CalculateCheckSum(fileName2)

    if (ret1 == ret2):
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()