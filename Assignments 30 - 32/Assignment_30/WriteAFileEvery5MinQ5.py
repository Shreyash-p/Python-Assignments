import schedule
import time
import datetime

def WriteInFile():
        try:
            fobj = open("Marvellous.txt", "a")

            if ( int((datetime.datetime.now()).strftime("%H")) > 12):
                fobj.write(f"Task executed at: {(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")} PM\n")
            else:
                fobj.write(f"Task executed at: {(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")} AM\n") 

            fobj.close()
        
        except Exception as e:
             print(f"ERROR: {e}")
        


def main():
    '''
    5: Schedule a task that executes every five minutes.
    The task should write the current date and time into a file named:
    Marvellous.txt
    New entries should be appended without removing previous entries.
    Example file contents:
    Task executed at: 25-07-2026 04:30:00 PM
    Task executed at: 25-07-2026 04:35:00 PM
    Task executed at: 25-07-2026 04:40:00 PM
    '''

    schedule.every(5).minutes.do(WriteInFile)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()