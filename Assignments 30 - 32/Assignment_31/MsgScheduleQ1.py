import schedule
import time
import sys

def Display(msg):
    print(msg)

def main():
    '''
    1: Write a program that accepts:
    • A message from the user
    • A time interval in seconds
    Schedule the program to display the message repeatedly after the specified interval.
    Example input:
    Enter message: Jay Ganesh
    Enter interval in seconds: 5
    Expected output:
    Jay Ganesh
    every five seconds.

    Validate that the interval is greater than zero.
    '''

    if (len(sys.argv) == 3 and int(sys.argv[2]) > 0):
        msg = sys.argv[1]
        timeInterval = int(sys.argv[2])
    else:
        print("Please provide 2 inputs")
        print("Input 1: A message to print")
        print("Input 2: A time interval in seconds greater than 0")

        sys.exit(1)

    schedule.every(timeInterval).seconds.do(Display, msg)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()