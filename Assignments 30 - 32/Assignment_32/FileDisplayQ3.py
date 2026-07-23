import schedule
import time
import sys
import os
import datetime

def FileDisplay(fileName):
    
    try:
        if not os.path.exists(fileName):
            print("Status: Error — File does not exist.")
            return

        fobj = open(fileName, "r")
        content = fobj.read()
        fobj.close()

        if len(content.strip()) == 0:
            print("Status: File is empty.")
        else:
            print("--- File Contents ---")
            print(content)
            print("---------------------")

    except PermissionError:
        print("Status: Error — Permission denied. Cannot read file.")
    except OSError as oe:
        print(f"Status: Error — File cannot be opened ({oe}).")
    except Exception as e:
        print(f"Status: Unexpected Error — {e}")


def main():
    '''
    3: Write a program that reads and displays the contents of a specified text file every minute.
    Handle the following conditions:
    • File does not exist
    • File is empty
    • Permission is denied
    • File cannot be opened
    '''

    fileName = r"C:\Users\patil\Desktop\Marvellous Infosystem\Assignments\Assignments 30 - 32\Assignment 32\FileEveryMinQ1.py"

    schedule.every(1).minutes.do(FileDisplay, fileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()