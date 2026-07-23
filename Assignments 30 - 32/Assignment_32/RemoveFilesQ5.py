import schedule
import time
import os
import datetime

def DeleteEmptyFiles(targetDir, logFileName):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    deleted_count = 0

    try:
        fobj = open(logFileName, "a")
        fobj.write(f"\n=== Cleanup Run: {timestamp} ===\n")

        for root, dirs, files in os.walk(targetDir):
            for file in files:
                filePath = os.path.join(root, file)

                try:
                    if os.path.exists(filePath) and os.path.getsize(filePath) == 0:
                        os.remove(filePath)
                        deleted_count += 1
                        
                        logMsg = f"DELETED: '{filePath}'\n"
                        print(f"Deleted empty file: {filePath}")
                        fobj.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {logMsg}")

                except PermissionError:
                    logMsg = f"FAILED: Permission denied for '{filePath}'\n"
                    print(f"Error: Permission denied for '{filePath}'")
                    fobj.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {logMsg}")
                except Exception as e:
                    logMsg = f"FAILED: Unexpected error on '{filePath}' ({e})\n"
                    print(f"Error on '{filePath}': {e}")
                    fobj.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {logMsg}")

        if deleted_count == 0:
            fobj.write("STATUS: No empty (0-byte) files found.\n")
            print("No empty files found.")

        fobj.write("-" * 50 + "\n")

        fobj.close()

    except Exception as e:
        print(f"Error writing to log file: {e}")
            


def main():
    '''
    5: Write a program that deletes all empty files from a specified directory every hour.
    The program should:
    • Scan the directory recursively
    • Detect files whose size is zero bytes
    • Delete the empty files
    • Store deleted file paths in a log file
    • Handle permission errors
    Test the program only on a sample directory.
    '''

    targetDir = r"C:\Users\patil\Desktop\Marvellous Infosystem\Assignments\Assignments 30 - 32\Assignment 32\Test"
    logFileName = "DeletedEmptyFilesLog.txt"

    schedule.every(1).hours.do(DeleteEmptyFiles, targetDir, logFileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()