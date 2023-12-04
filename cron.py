import schedule
import time
from datetime import datetime
import requests


def my_scheduled_job():
    url_to_request = "http://localhost:8000/image/"

    response = requests.post(url_to_request)


schedule.every(1).minutes.do(my_scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(1)
