import schedule
import time
import sys
import os
import datetime

def DirScanner(dirPath):
    print(f"Directory scanned: {os.path.split(dirPath)[-1]}")
    
    subfCtr = 0
    fileCtr = 0
    
    for FolderName, SubFolder, FileName in os.walk(dirPath):
        for subf in SubFolder:
            subfCtr += 1
    
        for fname in FileName:
            fileCtr += 1

    print(f"Total Files: {fileCtr}")
    print(f"Total Subdirectories: {subfCtr}")
    print(f"Scan time: {(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")}")
    print()


def main():
    '''
    3: Write a program that scans a specified directory every minute.
    The task should display:
    • Directory name
    • Number of files
    • Number of subdirectories
    • Date and time of scanning
    Use the os module.
    Example output:
    Directory Scanned: E:/Data
    Total Files: 15
    Total Subdirectories: 4
    Scan Time: 25-07-2026 04:30:00 PM
    '''

    dirPath = r"C:\Users\patil\Desktop\Marvellous Infosystem\Assignments\Assignments 30 - 32\Assignment 31\Test Dir"

    schedule.every(1).minutes.do(DirScanner, dirPath)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()