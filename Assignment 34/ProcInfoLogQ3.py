import os
import sys
import psutil
import datetime
import schedule
import time


def dirCreator(logDirName):
    try:
        if (os.path.exists(logDirName) == False):
            os.mkdir(logDirName)

    except Exception as e:
        print(f"ERROR : {e}")


def logWriter(logDirName, listProcess, errorMessage=None):

    dirCreator(logDirName)

    Border = "-" * 50
    logFileName = f"RunningProcessLog_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"

    with open(os.path.join(logDirName, logFileName), "w") as fobj:
        fobj.write(Border + "\n")
        
        if errorMessage != None:
            fobj.write(f"ERROR OCCURRED : {errorMessage}\n")

        else:
            for info in listProcess:
                fobj.write(f"PID            : {info.get('pid')}\n")
                fobj.write(f"Name           : {info.get('name')}\n")
                fobj.write(f"Username       : {info.get('username')}\n")
                fobj.write(Border + "\n")
        
        fobj.write(Border + "\n")


def runningProcessIndo(logDirName):
    listProcessData = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username"])
            listProcessData.append(pinfo)

        except Exception as e:
            logWriter(logDirName, errorMessage=e)

    logWriter(logDirName, listProcess=listProcessData)


def main():
    if (len(sys.argv) == 2):
        runningProcessIndo(sys.argv[1])
    elif (len(sys.argv) != 2):
        print("ERROR : Invalid Number of arguments\n")
        print("Please check usage :\n")
        print(f"python {sys.argv[0]} LogFolderName\n")


if __name__ == "__main__":
    main()