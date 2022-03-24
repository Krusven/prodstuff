
#Website Checker

##Table of contents
- [Purpose of this script](#purpose-of-this-script)
- [Installation](#installation)
  

## Requirements
- Windows: The script uses a vbs script and a bat file to run the python script.
- pip install requests win10toast
  - requests is needed to make the requests to the url
  - win10toast is used to create the windows 10 notifications

## Purpose of this script
This script makes a simple request to a url provided in the code and creates a Notification on the returned status.\
There are currently three different notifications possible:\
- 200: Website is running and a valid SSL certificate is provided.
- 404: Website is down or could not be reached.
- Every other status. Status code will be shown in the notification.

## Installation


