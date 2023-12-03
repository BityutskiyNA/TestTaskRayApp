import schedule
import time
from datetime import datetime
import requests


def my_scheduled_job():
    url_to_request = "http://127.0.0.1:8000/image/"
    username = "admin"
    password = "admin"
    auth = (username, password)

    response = requests.post(url_to_request)
    print(f'{datetime.now()}   {response.text}')



schedule.every(1).minutes.do(my_scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(1)
