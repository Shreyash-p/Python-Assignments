import os
import sys
import psutil
import datetime
import schedule
import time
import smtplib
from email.message import EmailMessage


def sendMail(sender, app_password, receiver, subject, body, logFileName):

    msg = EmailMessage()
    
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    msg.set_content(body)

    try:
        fobj = open(logFileName, "rb")
        msg.add_attachment(fobj.read(), maintype="application", subtype="octet-stream", filename=logFileName)
        fobj.close()
        
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        
        smtp.login(sender, app_password)
        
        smtp.send_message(msg)

        smtp.quit()

    except FileNotFoundError:
        print(f"Error: Log file '{logFileName}' was not found.")
        sys.exit(1)
    except smtplib.SMTPAuthenticationError:
        print("Error: Invalid email or app password.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: occurred while sending mail: {e}")
        sys.exit(1)


def dirCreator(logDirName):
    try:
        if (os.path.exists(logDirName) == False):
            os.mkdir(logDirName)

    except Exception as e:
        print(f"ERROR : {e}")
        sys.exit(1)


def logWriter(logDirName, listProcess, sender, app_password, receiver, subject, body, errorMessage=None):

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

    sendMail(sender, app_password, receiver, subject, body, os.path.join(logDirName, logFileName))


def runningProcessIndo(logDirName, sender, app_password, receiver, subject, body):
    listProcessData = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username"])
            listProcessData.append(pinfo)

        except Exception as e:
            logWriter(logDirName, sender, app_password, receiver, subject, body, errorMessage=e)

    logWriter(logDirName, listProcessData, sender, app_password, receiver, subject, body)


def main():

    if (len(sys.argv) == 3):

        sender = "_________________@gmail.com"

        app_password = "xxxx xxxx xxxx xxxx"

        subject = f"Duplicate File Removal Report - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}"

        body = f"""Jay Ganesh,

    Currently running processess log are created and stored at {sys.argv[1]} successfully.

    Task Details:
        - Target Directory: {sys.argv[1]}
        - Execution Time: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

    Please find the detailed log file attached to this email.

    Regards,
    Shreyash Patil
        """

        runningProcessIndo(sys.argv[1], sender, app_password, sys.argv[2], subject, body)

    elif (len(sys.argv) != 3):
        print("ERROR : Invalid Number of arguments\n")
        print("Please check usage :\n")
        print(f"python {sys.argv[0]} LogFolderName Recipient Email\n")


if __name__ == "__main__":
    main()
