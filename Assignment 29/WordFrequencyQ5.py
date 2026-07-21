import sys

def main():

    '''
    Q5) Frequency of a String in File
    Problem Statement:
    Write a program which accepts a file name and one string from the user and returns the frequency 
    (count of occurrences) of that string in the file.
    Input:
    Demo.txt Marvellous
    Expected Output:
    Count how many times "Marvellous" appears in Demo.txt.
    '''
    fileName = sys.argv[1]
    WordToSearch = sys.argv[2]

    try:
        fobj = open(fileName, "r")

        wordSum = 0

        for line in fobj:
            lst = line.split()

            for words in lst:
                if (WordToSearch == words):
                    wordSum = wordSum + 1


        print(f"Word count for {WordToSearch} in file {fileName} is: {wordSum}")

        fobj.close()
    
    except FileNotFoundError as fe:
        print("File not found")

if __name__ == "__main__":
    main()