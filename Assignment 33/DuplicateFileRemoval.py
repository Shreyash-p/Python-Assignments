#######################################################################################
# 
#   Importing required libraries
# 
#######################################################################################
import os
import sys
import schedule
import time
import datetime
from FileCleanerModule import run_job

#######################################################################################
# 
#   Function name :    main
#   Input :            Command line arguments
#   Description :      It controls the script
#   Date :             27/07/2026
#   Author :           Shreyash Suresh Patil
# 
#######################################################################################
def main():

    border = "=" * 50

    if (len(sys.argv) == 2 and sys.argv[1].lower() in ["--h", "--help", "--u", "--usage"]):
        print(f"\n{border}")
        print("--- Duplicate File Removal Automation Script ---")
        print(f"Usage: python {sys.argv[0]} <Directory_Path> <Interval_In_Minutes> <Recipient_Email>")
        print("Note: <Directory_Path> should be an absolute path.")
        print(f"{border}\n")
        sys.exit(0)

    if (len(sys.argv) != 4):
        print(f"\n{border}")
        print("Error: Invalid number of arguments.")
        print(f"Type 'python {sys.argv[0]} <--help/--h/--u/--usage>' for usage instructions.")
        print(f"{border}\n")
        sys.exit(1)

    src_dir = sys.argv[1]
    interval_in_min = int(sys.argv[2])
    recipient_email = sys.argv[3]

    schedule.every(interval_in_min).minutes.do(run_job, src_dir, interval_in_min, recipient_email)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as e:
        sys.exit(1)

#######################################################################################
# 
#   Starter of the automation script
# 
#######################################################################################
if __name__ == "__main__":
    main()
