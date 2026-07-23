import schedule
import time

def Display():
        print(f"Coding Kar..!")             


def main():
    '''
    3: Write a program that schedules a function to print:
    Coding Kar..!
    every 30 minutes.
    '''

    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(100)



if __name__ == "__main__":
    main()