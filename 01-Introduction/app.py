from locust import User, task, constant


class MyFirstTest(User):
    weight = 1
    wait_time = constant(2)

    @task
    def launch(self):
        print("1st URL Launch")

    @task
    def search(self):
        print("1st search...")


class MySecondTest(User):
    weight = 2
    wait_time = constant(4)

    @task
    def launch2(self):
        print("2nd URL launch")

    @task
    def search2(self):
        print("2nd search....")