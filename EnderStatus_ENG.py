import requests
import time
import os
from termcolor import colored

#Api developed by Fyks

#Ender Project
#Discord : https://discord.gg/y8pCwzaR
#Web : endertopluluk.com

#Api Expire : 3.10.2023 | For the new API: scriptkidsensei

url = "https://api.uptimerobot.com/v2/getMonitors"

payload = "api_key=m795389648-f88c0335344438cfa62151c3&format=json&logs=1"
public = "m795389648-f88c0335344438cfa62151c3"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

ender = """


                     ███████╗███╗   ██╗██████╗ ███████╗██████╗
                     ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
                     █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
                     ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
                     ███████╗██║ ╚████║██████╔╝███████╗██║  ██║
                     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

"""
os.system('clear')
print(ender)
print(f"                   Endertopluluk.com Real-time Status |  API : ... ")
time.sleep(3)
os.system('clear')
print(ender)
print("")
print(f"                   Endertopluluk.com Real-time Status |  API : {colored(public, 'magenta')} ")

try:
    response = requests.request("POST", url, data=payload, headers=headers)
    response.raise_for_status()

    data = response.json()


    apis = data.get("monitors")

    print(f" [...] Checking endertopluluk.com | {colored(public, 'magenta')} | {colored('uptime', 'green')}")
    time.sleep(2)

    for api in apis:
        status = api.get("status")
        api_is = api.get("friendly_name")
        location = api.get("logs")[-1].get("location")
        last_check = api.get("logs")[-1].get("datetime")
        last_check_timestamp = api.get("logs")[-1].get("datetime")
        last_check = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(last_check_timestamp))
        if status == 2:
            print("")
            print(f" [{colored('+', 'green')}] {api_is} is Running! API Status: {colored(status, 'yellow')} | Last Check: {last_check}")
            print("")
        else:
            print(f"[{colored('-', 'red')}] {api_is} is Down! | Info: discord.gg/y8pCwzaR | API status: {status}")
            print(f"Last Check: {last_check}")

except requests.exceptions.RequestException as e:
    print(f"[-] Error: {e}")
except requests.exceptions.HTTPError as e:
    print(f"[-] HTTP Error: {e}")
