
#Website Checker

##Table of contents
- [Requirements](#requirements)
- [Purpose of this script](#purpose-of-this-script)
- [Installation](#installation)
  

## Requirements
- Windows: The script uses a vbs script and a bat file to run the python script.
- pip install requests win10toast
  - requests is needed to make the requests to the url
  - win10toast is used to create the windows 10 notifications

## Purpose of this script
This script makes a simple request to a url provided in the code and creates a Windows 10 style notification with the returned status.\
There are currently three different notifications possible:\
- <span style="color: lightgreen">200</span>: Website is running and a valid SSL certificate is provided. 
- <span style="color: tomato">404</span>: Website is down or could not be reached.
- <span style="color: #7FFFD4">Every other status</span>: Status code will be shown in the notification.

- The reason for the .vbs file is to minimize the cmd window when the process is running. This is not possible from within the .bat file, so the. vbs file is used to run the .bat file with a minimized cmd window
  - The alternative would have been to select "Run whether user is logged on or not", but this option seems to mute the notifications so the .vbs file is the simplest alternative solution

## Installation
1. Install requirements, see [Requirements](#requirements)
2. Configure paths:
   1. Add correct path to .bat file in the .vbs file
   2. Add correct paths to python and .py file in .bat file
      1. The python file can be run from a virtual environment, just configure path to be <span style="color:#7FFF00">"venv\Scripts\python.exe"</span>
3. Create a Scheduled Task with the following properties: 
   1. "Run only when user is logged in"
      1. For some reason the notifications do not show up when run using "Run whether user is logged on or not"
   2. Choose preferred Triggers
   3. In the Actions tab 
      1. Program/script: cmd
      2. Add Arguments (optional): /c start cscript //nologo "D:\path\to\vbsfile.vbs"
   4. Save


