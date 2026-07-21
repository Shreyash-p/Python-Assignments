import sys

def main():

    '''
    Q1) Count Lines in a File
    Problem Statement:
    Write a program which accepts a file name from the user and counts how many lines are present in the file.
    Input: Demo.txt
    Expected Output: Total number of lines in Demo.txt.
    '''
    fileName = sys.argv[1]

    try:
        fobj = open(fileName, "r")

        print(f"Total number of lines in {fileName} is: {len(fobj.readlines())}")

        fobj.close()
    
    except FileNotFoundError as fe:
        print("File not found")

if __name__ == "__main__":
    main()