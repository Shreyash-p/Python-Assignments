import schedule
import time
import sys
import os
import datetime

def DirScanner(dirPath):
    fileCtr = 0

    for FolderName, SubFolder, FileName in os.walk(dirPath):
        for fname in FileName:
            fileCtr += 1

    fileName = "DirectoryCountLog.txt"

    fobj = open(fileName, "w")

    fobj.write(f"Directory path: {dirPath}\n")
    fobj.write(f"Total Files: {fileCtr}\n")
    fobj.write(f"Scan time: {(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")}\n")


def main():
    '''
    5:Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.
    Write the result into:
    DirectoryCountLog.txt
    Each entry should contain:
    • Directory path
    • Number of files
    • Date and time
    '''

    if (len(sys.argv) == 2 and os.path.isdir(sys.argv[1])):
        dirName = sys.argv[1]
    else:
        print("Please provide 1 input")
        print("Input 1: A directory path")
    
        sys.exit(1)

    schedule.every(5).minutes.do(DirScanner, dirName)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()