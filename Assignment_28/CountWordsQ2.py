import sys

def main():

    '''
    Q2) Count Words in a File
    Problem Statement:
    Write a program which accepts a file name from the user and counts the total number of words in that file.
    Input: Demo.txt
    Expected Output: Total number of words in Demo.txt.
    '''
    fileName = sys.argv[1]

    try:
        fobj = open(fileName, "r")

        wordSum = 0

        for line in fobj.readlines():
            lst = line.split()
            print(lst)
            wordSum = wordSum + len(lst)


        print(f"Total number of words in {fileName} is: {wordSum}")

        fobj.close()
    
    except FileNotFoundError as fe:
        print("File not found")

if __name__ == "__main__":
    main()