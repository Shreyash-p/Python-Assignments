# 📁 Automated Duplicate File Remover & Mailer

A modular Python automation tool that periodically scans a target directory, identifies duplicate files using MD5 checksum matching, safely removes extra copies, and automatically emails a detailed execution log to a specified address.

---

## 📌 Features

* 🔍 **Checksum Matching:** Uses MD5 hashing to accurately identify identical file contents regardless of filename.
* 🗑️ **Automated Cleanup:** Retains the original file and deletes duplicate copies.
* 🕒 **Periodic Scheduling:** Built-in scheduler using Python's `schedule` library to run job cycles at user-defined minute intervals.
* 📧 **Automated Email Reports:** Delivers timestamped execution logs as email attachments via Gmail SMTP.
* 🛡️ **Input Validation & Safety:** Validates directory existence, absolute paths, and time intervals before running.

---

## 🛠️ Project Structure

```text
├── DuplicateFileRemoval.py     # Entry point (handles CLI arguments & job scheduling)
├── FileCleanerModule.py        # Core engine (checksum, file removal, logging & email logic)
├── Marvellous_Log/             # Auto-generated directory for timestamped log reports
└── README.md                   # Documentation
