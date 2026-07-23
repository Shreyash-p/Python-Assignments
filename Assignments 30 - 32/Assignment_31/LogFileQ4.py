import schedule
import time
import sys
import os
import datetime

def LogFileCreator():
    timestamp = (datetime.datetime.now()).strftime("%d_%m_%Y_%H_%M_%S")
    fileName = f"Marvellous_Log_{timestamp}"

    fobj = open(fileName, "w")

    fobj.write(f"Creation time: {timestamp}\n")


def main():
    '''
    4: Write a program that creates a new log file after every ten minutes.
    The filename should contain the current date and time.
    Example:
    MarvellousLog_25_07_2026_16_30_00.txt
    The file should contain:
    Log file created successfully.
    Creation Time: 25-07-2026 04:30:00 PM
    '''

    schedule.every(1).minutes.do(LogFileCreator)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()