import os
import sys
import psutil
import datetime
import schedule
import time


def logWriter(listProcess=None, errorMessage=None):
    Border = "-" * 50
    logFileName = f"RunningProcessLog_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"

    with open(logFileName, "w") as fobj:
        fobj.write(Border + "\n")
        
        if errorMessage != None:
            fobj.write(f"ERROR OCCURRED : {errorMessage}\n")
        
        elif listProcess == None:
            fobj.write("ERROR : Invalid Number of arguments\n")
            fobj.write("Please check usage :\n")
            fobj.write(f"python {sys.argv[0]} ProcessName\n")

        else:
            if len(listProcess) == 0:
                fobj.write("No matching process found.\n")
            else:
                for info in listProcess:
                    fobj.write(f"PID            : {info.get('pid')}\n")
                    fobj.write(f"Name           : {info.get('name')}\n")
                    fobj.write(f"Username       : {info.get('username')}\n")
                    fobj.write(f"Status         : {info.get('status')}\n")
                    fobj.write(f"CPU Percent    : {info.get('cpu_percent'):.2f}\n")
                    fobj.write(f"Memory Percent : {info.get('memory_percent'):.2f}\n")
                    fobj.write(Border + "\n")
        
        fobj.write(Border + "\n")


def runningProcessIndo(procName):
    listProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username", "status"])
            
            if (pinfo["name"].lower() == procName.lower() or (pinfo["name"].split(".")[0]).lower() == procName.lower()):
                pinfo["cpu_percent"] = proc.cpu_percent()
                pinfo["memory_percent"] = proc.memory_percent()
                listProcess.append(pinfo)

        except Exception as e:
            logWriter(e)

    logWriter(listProcess)


def main():
    if (len(sys.argv) == 2):
        runningProcessIndo(sys.argv[1])
    elif (len(sys.argv) != 2):
        logWriter()


if __name__ == "__main__":
    main()