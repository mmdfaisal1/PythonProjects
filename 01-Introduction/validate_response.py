from locust import HttpUser, SequentialTaskSet, task, constant


class MySequentialTaskSet(SequentialTaskSet):

    @task
    def task_1(self):
        print("Starting task 1")

        # print("Got task 1 response status:", response.status_code)

    @task
    def task_two(self):
        payload = {
            "name": "blah_name",
            "job": "blah_job"
        }
        print("Starting task 2")


class MyLoadTest(HttpUser):
    host = "https://resreq.in"
    tasks = [MySequentialTaskSet]
    wait_time = constant(2)
