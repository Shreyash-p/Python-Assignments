import sys

def main():

    '''
    Q5) Search a Word in File
    Problem Statement:
    Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
    Input:
    Demo.txt Marvellous
    Expected Output:
    Display whether the word Marvellous is found in Demo.txt or not.
    '''
    fileName = sys.argv[1]
    WordToSearch = sys.argv[2]

    try:
        fobj = open(fileName, "r")

        flag = False
        for line in fobj:
            lst = line.split()
            for word in lst:
                if (WordToSearch == word):
                    flag = True


        if (flag == True):
            print(f"Word {WordToSearch} is found")
        else:
            print(f"Word {WordToSearch} is not found")


        fobj.close()
    
    except FileNotFoundError as fe:
        print("File not found")

if __name__ == "__main__":
    main()