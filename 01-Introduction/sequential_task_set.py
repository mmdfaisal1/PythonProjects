from locust import SequentialTaskSet, task, constant, User
from locust.exception import StopUser


class MySequentialTaskSet(SequentialTaskSet):

    @task
    def find_flight(self):
        print("I am finding flight")

    @task
    def select_flight(self):
        print("I am selecting flight")

    @task
    def book_flight(self):
        print("I am booking flight")
        # It will exit the current user e.g. user is unable to login
        raise StopUser()


class MyTest(User):
    tasks = [MySequentialTaskSet]
    wait_time = constant(1)
