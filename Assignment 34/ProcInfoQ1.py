import os
import sys
import psutil
import datetime
import schedule
import time


def logWriter(listProcess):
    Border = "-" * 50

    logFileName = f"RunningProcessLog{datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}"

    with open(logFileName, "w") as fobj:
        for info in listProcess:
            fobj.write(Border + "\n")
            fobj.write(f"PID : {info.get("pid")}\n")
            fobj.write(f"Name : {info.get("name")}\n")
            fobj.write(f"Username : {info.get("username")}\n")
            fobj.write(f"Status : {info.get("status")}\n")
            fobj.write(f"CPU Percent : {info.get("cpu_percent")}:.2f\n")
            fobj.write(f"Memory Percent : {info.get("memory_percent")}:.2f\n")
            fobj.write(Border + "\n")


def runningProcessIndo():
    listProcess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "username", "status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listProcess.append(info)

    logWriter(listProcess)


def main():
    runningProcessIndo()


if __name__ == "__main__":
    main()