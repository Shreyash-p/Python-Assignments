import schedule
import time
import datetime

def LunchTime():
        print(f"Lunch Time!.")

def WrapUpTime():
        print(f"Wrap up work.")
        


def main():
    '''
    6: Write a script that schedules the following tasks:
    • Print Lunch Time! every day at 1:00 PM.
    • Print Wrap up work every day at 6:00 PM.
    Both tasks should be handled by separate functions.
    '''

    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUpTime)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()