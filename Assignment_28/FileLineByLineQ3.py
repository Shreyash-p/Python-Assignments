import sys

def main():

    '''
    Q3) Display File Line by Line
    Problem Statement:
    Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
    Input: Demo.txt
    Expected Output: Display each line of Demo.txt one by one.
    '''
    fileName = sys.argv[1]

    try:
        fobj = open(fileName, "r")

        for line in fobj:
            print(line)

        fobj.close()
    
    except FileNotFoundError as fe:
        print("File not found")

if __name__ == "__main__":
    main()