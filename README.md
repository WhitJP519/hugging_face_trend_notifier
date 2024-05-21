# Hugging Face Trending Models Notifier

This project provides a Python script that periodically checks for the top trending models on Hugging Face and sends desktop notifications with the details of the top 3 models. The script is designed to run in the background without opening a command prompt window, making it unobtrusive and user-friendly.

## Features

- **Automated Notifications**: The script automatically checks for updates in trending models and sends notifications every hour.
- **Detailed Notifications**: Each notification includes the model name and author for the top 3 trending models.
- **Background Execution**: The script runs in the background without opening a command prompt window, thanks to a helper utility.
- **Robust Logging**: Logs are maintained for each run, capturing details about the script's execution and any errors that occur.
- **Cross-Platform Libraries**: Utilizes `requests` for HTTP requests, `BeautifulSoup` for HTML parsing, and `win10toast` for Windows notifications.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `win10toast` library
- `nircmd` utility for hidden execution

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/WhitJP519/hugging_face_trend_notifier.git
   cd hf_trending_models_notifier
2.**Install Dependencies**:

bash
Copy code
pip install requests beautifulsoup4 win10toast
3.**Download nircmd.exe**:

Download nircmd.exe from NirSoft's website.
Save nircmd.exe to a location you can easily access (e.g., C:\path\to\nircmd).

4.**Create the Batch File**:

Open Notepad or any text editor.
Enter the following commands, replacing the paths with your actual paths:
bat
Copy code
@echo off
cd /d "C:\path\to\your\script\directory"
C:\path\to\nircmd\nircmd.exe exec hide "C:\Program Files\Python312\python.exe" "C:\path\to\your\script\directory\hf_trending_models_notifier.py"
Save the file as run_notifier_hidden.bat.

5.**Set Up Task Scheduler**:

Open Task Scheduler (taskschd.msc).
Create a new task or update an existing task with the following settings:
General:
Name: Hugging Face Notifier
Check "Run only when user is logged on".
Triggers:
New trigger set to "Daily" and repeat every "1 hour".
Actions:
Start a program: C:\path\to\your\run_notifier_hidden.bat.
Conditions:
Uncheck "Start the task only if the computer is on AC power".
Settings:
Check "Allow task to be run on demand".
Check "Run task as soon as possible after a scheduled start is missed".
