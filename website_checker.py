import requests
from win10toast import ToastNotifier

def url_checker():
    #Enter your URL here
    url = "https://www.svenchristiankruse.me"
    try:
        #make request to specified url
        get = requests.get(url, verify=True)

        #create Toast for 200 code
        if get.status_code == 200:
            title = "Website working"
            string = f"{url}: is up and running and has valid SSL certificate"
            toaster(title, string)
            return
            
        #create Toast for 404 code
        elif get.status_code == 404:
            title = "Website NOT working"
            string = f"{url}: website is down with status code 404"
            toaster(title, string)
            return
            
        #create Toast for all other codes and give status code in Toast
        else:
            title = "Website down"
            string = f"{url}: is NOT working, status code: {get.status_code}"
            toaster(title, string)
            return
            
    #catch exception if something goes wrong with the request
    #Note: no Toast is created in this case
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url}: is Not reachable or has no valid SSL certificate \nErr: {e}")

#function that creates toast using a title and string and icon
def toaster(title, string):
    toaster = ToastNotifier()
    toaster.show_toast(title,
    string,
    icon_path="D:\Software Dev\prodstuff\web_icon.ico",
    duration=30)


url_checker()
