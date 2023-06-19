from datetime import datetime
from locust import User, task, constant, between


class MyUser(User):
    wait_time = between(2, 5)

    @task
    def launch(self):
        print("This will inject a delay of between 2 and 5 seconds\nCurrent time is:", datetime.now())

