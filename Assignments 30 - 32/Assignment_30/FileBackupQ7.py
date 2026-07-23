import schedule
import time
import datetime
import shutil
import sys
import os

def FileBackup(SrcFilePath, DestiPath):
    Border = "=" * 50
    sourceFileName = os.path.split(SrcFilePath)[-1]
    Name = sourceFileName.split(".")[0]
    extension = sourceFileName.split(".")[1]
    timestamp = (datetime.datetime.now()).strftime("%Y%m%d%H%M%S")
    BackupFileName = Name + "_" + timestamp + "." + extension
    DestiFilePath = os.path.join(DestiPath, BackupFileName)
    

    try:
        shutil.copy(SrcFilePath, DestiFilePath)

        print("File copied to destination path")

        fobj = open("backup_log.txt", "a")

        fobj.write(f"Backup filename: {BackupFileName}\n")
        fobj.write(f"Example log entry: Backup completed successfully at {datetime.datetime.now()}\n")
        fobj.write(Border + "\n")

        print("Entry added in log file")

        fobj.close()

        print("File backup complete.")
        
    except Exception as e:
        print("Error:", e)


def main():
    '''
        7: Write a Python program that performs a file backup every hour.
        The program should:
        1. Accept the source file path.
        2. Accept the destination directory path.
        3. Copy the source file to the destination directory.
        4. Add the current date and time to the backup filename.
        5. Write the backup operation details into: backup_log.txt
        Example 
        backup filename: Data_25_07_2026_16_30_00.txt
        Example log entry: Backup completed successfully at 25-07-2026 04:30:00 PM
        Use the shutil module for file copying.
    '''

    SrcFilePath = sys.argv[1]
    DestiPath = sys.argv[2]

    if (os.path.isdir(DestiPath) and os.path.isfile(SrcFilePath)):
        print("Starting file backup process")
        schedule.every(10).seconds.do(FileBackup, SrcFilePath, DestiPath)
    else:
        print("Please provide valid inputs")
        print("Input 1: Input file path")
        print("Input 2: Backup Directory path")
        sys.exit(1)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()