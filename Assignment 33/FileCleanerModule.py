#######################################################################################
# 
#   Importing required libraries
# 
#######################################################################################
import os
import sys
import time
import datetime
import hashlib
import smtplib
from email.message import EmailMessage


border = "=" * 50

#######################################################################################
# 
#   Function name :     logDirCreator
#   Input :             logFilePath (str)
#   Description :       Creates the target directory for storing log files if missing
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
def logDirCreator(logFilePath):
    if (os.path.exists(logFilePath) == False):
        os.mkdir(logFilePath)


#######################################################################################
# 
#   Function name :     logWriter
#   Input :             fileName (str), msg (str)
#   Description :       Appends a text message line to the specified log file
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
def logWriter(fileName, msg):

    with open(fileName, "a", encoding="utf-8") as logobj:
        logobj.write(msg + "\n")


#######################################################################################
# 
#   Function name :     calculateCheckSum
#   Input :             FileName (str)
#   Description :       Calculates and returns the MD5 hash checksum of a given file
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
def calculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


#######################################################################################
# 
#   Function name :     validateInputs
#   Input :             dirName (str), timeInterval (int), emailId (str), logFileName (str)
#   Description :       Validates input directory path and schedule interval parameters
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
def validateInputs(dirName, timeInterval, emailId, logFileName):
    exitFlag = True
    if (timeInterval <= 0):
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, "Error: Interval must be a positive number greater than 0.")
        logWriter(logFileName, f"{border}\n")
        exitFlag = False

    if (os.path.exists(dirName) == False):
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, "Error: The specified directory path does not exist or is invalid.")
        logWriter(logFileName, "Note: <Directory_Path> should be an absolute path.")
        logWriter(logFileName, f"{border}\n")
        exitFlag = False

    if (os.path.isdir(dirName) == False):
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, "Error: The specified directory is not a directory.")
        logWriter(logFileName, f"{border}\n")
        exitFlag = False

    if (os.path.isabs(dirName) == False):
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, "Error: The specified directory path is not an absolute path.")
        logWriter(logFileName, f"{border}\n")
        exitFlag = False

        
    return exitFlag


#######################################################################################
# 
#   Function name :     checkFile
#   Input :             fileName (str), logFileName (str)
#   Description :       Verifies file existence and catches permissions or access errors
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
def checkFile(fileName, logFileName):
    try:
        if (os.path.isfile(fileName)):
            return True

    except PermissionError as pe:
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, f"Error: {fileName} - {pe}")
        logWriter(logFileName, f"{border}\n")
        return False

    except FileNotFoundError as fnfe:
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, f"Error: {fileName} - {fnfe}")
        logWriter(logFileName, f"{border}\n")
        return False

    except Exception as e:
        logWriter(logFileName, f"{border}")
        logWriter(logFileName, f"Error: {fileName} - {e}")
        logWriter(logFileName, f"{border}\n")
        return False


#######################################################################################
# 
#   Function name :     removeDuplicateFiles
#   Input :             dirName (str), logFileName (str)
#   Description :       Scans directory for duplicate files using MD5 hashes and deletes them
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
def removeDuplicateFiles(dirName, logFileName):
    startTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    checkSumDict = {}
    totalFileCount = 0
    dirScannedNames = []
    fileScannedNames = []

    logWriter(logFileName, f"{border}")
    logWriter(logFileName, f"{border}")
    logWriter(logFileName, f"Start time: {startTime}")
    logWriter(logFileName, f"{border}")

    for folderName, subFolderName, fileName in os.walk(dirName):
        dirScannedNames.append(os.path.split(folderName)[-1])

        for fname in fileName:
            fname = os.path.join(folderName, fname)
            totalFileCount = totalFileCount + 1

            fileChecker = checkFile(fname, logFileName)

            if (fileChecker == False):
                continue

            checkSumValue = calculateCheckSum(fname)

            if (checkSumValue in checkSumDict):
                checkSumDict[checkSumValue].append(fname)
            else:
                checkSumDict[checkSumValue] = [fname]


    dublicateFileName = list(filter(lambda x : len(x) > 1, checkSumDict.values()))

    count = 0
    totalDeleted = 0

    for value in dublicateFileName:
        for subValue in value:
            count = count + 1
            if (count > 1):
                fileScannedNames.append(subValue)
                os.remove(subValue)
                totalDeleted = totalDeleted + 1
        count = 0


    logWriter(logFileName, f"\nDirectories that were scanned:")
    if dirScannedNames:
            logWriter(logFileName, "\n".join(dirScannedNames))
    logWriter(logFileName, f"\n{border}\n")
    logWriter(logFileName, f"Total number of duplicate files found: {totalDeleted}")
    logWriter(logFileName, f"\n{border}\n")
    logWriter(logFileName, f"Total number of duplicate files deleted: {totalDeleted}")
    logWriter(logFileName, f"\n{border}\n")
    logWriter(logFileName, f"Duplicate files:")
    if fileScannedNames:
        logWriter(logFileName, "\n".join(fileScannedNames))
    logWriter(logFileName, f"\n{border}")

    endTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    logWriter(logFileName, f"End time: {endTime}")
    logWriter(logFileName, f"{border}")
    logWriter(logFileName, f"{border}")


#######################################################################################
# 
#   Function name :     sendMail
#   Input :             sender (str), app_password (str), receiver (str), 
#                       subject (str), body (str), logFileName (str)
#   Description :       Sends an email report with the generated log file as an attachment
#   Date :              27/07/2026
#   Author :            Shreyash Suresh Patil
# 
#######################################################################################
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
        sys.exit(0)
    except smtplib.SMTPAuthenticationError:
        print("Error: Invalid email or app password.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: occurred while sending mail: {e}")
        sys.exit(0)            


#######################################################################################
# 
#   Function name :    DirectoryScanner
#   Input :            Name of Directory
#   Description :      Deletes all empty files periodically
#   Date :             27/07/2026
#   Author :           Shreyash Suresh Patil
# 
#######################################################################################
def run_job(src_dir, interval_in_min, recipient_email):
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    logFilePath = "Marvellous_Log"
    logFileName = os.path.join(logFilePath, f"DuplicateRemovalLog_{timestamp}.txt")

    logDirCreator(logFilePath)

    sender = "________________@gmail.com"

    app_password = "xxxx xxxx xxxx xxxx"

    subject = f"Duplicate File Removal Report - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}"

    body = f"""Jay Ganesh,

The duplicate file removal process has completed successfully.

Task Details:
    - Target Directory: {src_dir}
    - Execution Time: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

Please find the detailed log file attached to this email.

Regards,
Shreyash Patil
    """
    
    if validateInputs(src_dir, interval_in_min, recipient_email, logFileName):

        removeDuplicateFiles(src_dir, logFileName)

        sendMail(sender, app_password, recipient_email, subject, body, logFileName)

    else:
        print(f"ERROR: Invalid inputs. Check log file: {logFileName}")
        sys.exit(1)