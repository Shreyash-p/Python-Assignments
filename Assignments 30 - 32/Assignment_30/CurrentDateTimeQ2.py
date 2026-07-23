import schedule
import time
import datetime

def DisplayDateTime():
        if ( int((datetime.datetime.now()).strftime("%H")) > 12):
            print(f"Current Date and Time: {(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")} PM")
        else:
            print(f"Current Date and Time: {(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")} AM")             


def main():
    '''
    2: Write a Python program that displays the current date and time after every one minute.
    Use the datetime module.
    Expected output:
    Current Date and Time: 25-07-2026 04:30:00 PM
    '''

    schedule.every(1).minutes.do(DisplayDateTime)

    while True:
        schedule.run_pending()
        time.sleep(10)



if __name__ == "__main__":
    main()