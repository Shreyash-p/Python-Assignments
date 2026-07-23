import schedule
import time
import sys
import os
import datetime

def FileSizeLogCreator(fileName):

    f1 = open("FileEveryMinQ1.py", "r")
    fobj = open("FileSizeLog.txt", "w")

    fobj.write(f"Filename: {fileName}\n")
    fobj.write(f"Size: {os.path.getsize(fileName)}\n bytes")
    fobj.write(f"Creation time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")

    f1.close()
    fobj.close()


def main():
    '''
    2: Write a Python program that monitors the size of a specified file every 30 seconds.
    Write the following details into:
    FileSizeLog.txt
    • File path
    • File size in bytes
    • Date and time
    Handle the situation where the file does not exist.
    '''

    fileName = r"C:\Users\patil\Desktop\Marvellous Infosystem\Assignments\Assignments 30 - 32\Assignment 32\FileEveryMinQ1.py"

    schedule.every(30).seconds.do(FileSizeLogCreator, fileName)
    
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()