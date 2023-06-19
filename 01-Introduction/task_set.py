from locust import TaskSet, task, constant, User, HttpUser


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    # tasks = [MyTaskSetOne, MyTaskSetTwo]
    wait_time = constant(3)

    @task
    class MyTaskSetOne(TaskSet):
        @task
        def get_status(self):
            response = self.client.get("/200")
            print("Got response status:", response.status_code)
            # self.interrupt() is necessary for control to switch out of the class
            # reschedule = False for wait time to take affect
            self.interrupt(reschedule=False)

    @task
    class MyTaskSetTwo(TaskSet):
        @task
        def get_status(self):
            self.client.get("/404")
            # the above actually gives you 200
            print("Got response status 404")
            self.interrupt(reschedule=False)
