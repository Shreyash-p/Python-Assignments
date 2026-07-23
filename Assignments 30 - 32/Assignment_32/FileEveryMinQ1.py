import schedule
import time
import sys
import os
import datetime

def LogFileCreator():
    timestamp = (datetime.datetime.now()).strftime("%d_%m_%Y_%H_%M_%S")
    crtDate = (datetime.datetime.now()).strftime("%d-%m-%Y")
    crtTime = (datetime.datetime.now()).strftime("%H:%M:%S")
    fileName = f"File_{timestamp}.txt"

    fobj = open(fileName, "w")

    fobj.write(f"Filename: {fileName}\n")
    fobj.write(f"Creation date: {crtDate}\n")
    fobj.write(f"Creation time: {crtTime}\n")

    fobj.close()


def main():
    '''
    1: Write a program that creates a new text file every minute.
    The filename should contain the current timestamp.
    Example:
    File_25_07_2026_16_30_00.txt
    Write the following information into the file:
    • Filename
    • Creation date
    • Creation time
    '''

    schedule.every(1).minutes.do(LogFileCreator)
    
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()