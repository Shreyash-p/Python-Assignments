import sys

def main():

    '''
    Q4) Copy File Contents into Another File
    Problem Statement:
    Write a program which accepts two file names from the user.
    • First file is an existing file
    • Second file is a new file
    Copy all contents from the first file into the second file.
    Input:
    ABC.txt Demo.txt
    Expected Output:
    Contents of ABC.txt copied into Demo.txt.
    '''
    fileName1 = sys.argv[1]
    fileName2 = sys.argv[2]

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