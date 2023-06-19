from locust import HttpUser, constant, task


class MyHttpUserOne(HttpUser):

    host = "http://newtours.demoaut.com"
    wait_time = constant(2)
    weight = 3

    @task
    def login(self):
        print("Logging User One.......")


class MyHttpUserTwo(HttpUser):

    host = "http://newtours.demoaut.com"
    wait_time = constant(2)
    weight = 1

    @task
    def login(self):
        print("Logging User Two.......")