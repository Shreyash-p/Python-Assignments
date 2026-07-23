import schedule
import time
import os
import sys
import shutil
import datetime

def CopyTxtFiles(sourceDir, destDir, logFileName):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] Starting scheduled backup operation...")

    if not os.path.exists(sourceDir):
        print(f"Error: Source directory '{sourceDir}' does not exist.")
        return

    if not os.path.isdir(sourceDir):
        print(f"Error: Source path '{sourceDir}' is not a valid directory.")
        return

    txt_files_found = 0

    try:
        fobj = open(logFileName, "a")
        fobj.write(f"\n=== Backup Run: {timestamp} ===\n")

        for root, dirs, files in os.walk(sourceDir):
            for file in files:
                if file.lower().endswith(".txt"):
                    txt_files_found += 1
                    
                    srcPath = os.path.join(root, file)
                    destPath = os.path.join(destDir, file)

                    try:
                        shutil.copy2(srcPath, destPath)
                        logMsg = f"SUCCESS: Copied '{file}' from '{root}'\n"
                        print(f"Copied: {file}")
                    except Exception as e:
                        logMsg = f"FAILED: Unexpected error copying '{file}' ({e})\n"
                        print(f"Error copying '{file}': {e}")

                    fobj.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {logMsg}")

        if txt_files_found == 0:
            fobj.write("STATUS: No .txt files found to copy.\n")
            print("No .txt files found in source directory.")

        fobj.write("-" * 50 + "\n")

        fobj.close()

    except Exception as e:
        print(f"Error writing to log file: {e}")
            

def main():
    '''
    4: Write a program that copies all .txt files from one directory to another every ten minutes.
    The program should:
    • Accept source and destination directories
    • Validate both directories
    • Copy only .txt files
    • Maintain a log of copied files
    • Avoid terminating if one file cannot be copied
    '''

    sourceDir = sys.argv[1]
    destDir = sys.argv[2]
    logFileName = "CopyLog.txt"

    schedule.every(10).minutes.do(CopyTxtFiles, sourceDir, destDir, logFileName)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()