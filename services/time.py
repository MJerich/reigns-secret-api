# time.py

import requests


def current_time_request():
    url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles"
    response = requests.get(url=url)
    if response.status_code == 200:
        message = response.json()
        return message
    else:
        err_message = {
            "error": "Sorry, we received error."
        }
        return err_message


def current_year_request():
    url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles"
    response = requests.get(url=url)
    if response.status_code == 200:
        message = response.json()["year"]
        return message
    else:
        err_message = {
            "error": "Sorry, we received error."
        }
        return err_message
