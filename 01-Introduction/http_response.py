from time import sleep

from locust import HttpUser, constant, task, SequentialTaskSet, User


class MySequentialTaskSet(SequentialTaskSet):

    @task
    def get_user(self):
        response1 = self.client.get("/get")
        print(response1.status_code)

    @task
    def create_user(self):
        payload = {
            "name": "faisal",
        }
        response = self.client.post("/post", json=payload)
        print(response.text)


class MyHttpUser(HttpUser):

    host = "https://httpbin.org"
    wait_time = constant(4)
    tasks = [MySequentialTaskSet]


