from locust import TaskSet, task, User, constant
from locust.event import EventHook

my_event = EventHook()


@my_event.add_listener
def my_event_handler(a, b, **kwargs):
    print("Event was fired with", a, b)


class MyTaskSet(TaskSet):

    @task
    def task_1(self):
        print("Executing task#1")
        my_event.fire(a="apple", b="banana")


class MyUser(User):
    tasks = [MyTaskSet]
    wait_time = constant(3)

