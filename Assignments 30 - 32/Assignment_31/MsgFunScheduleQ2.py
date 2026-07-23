import schedule
import time
import sys

def DisplayMessage(msg):
    print(msg)

def main():
    '''
    2: Create a function named:
    DisplayMessage(message)
    Schedule the function using:
    schedule.every(5).seconds.do(DisplayMessage, message)
    The message should be accepted from the user.
    '''

    if (len(sys.argv) == 2):
        msg = sys.argv[1]
    else:
        print("Please provide 1 input")
        print("Input 1: A message to print")

        sys.exit(1)

    schedule.every(5).seconds.do(DisplayMessage, msg)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()