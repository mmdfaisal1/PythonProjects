from locust import HttpUser, constant, task


class MyHttpUser(HttpUser):

    host = "http://newtours.demoaut.com"
    wait_time = constant(2)

    @task
    def login(self):
        print("Logging in....")