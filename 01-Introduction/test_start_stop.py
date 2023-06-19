from locust import HttpUser, constant, task, events


@events.test_start.add_listener
def script_start(**kwargs):
    print("Starting the test")


@events.test_stop.add_listener
def script_finish(**kwargs):
    print("Finishing the test")


class MyHttpUser(HttpUser):

    host = "http://newtours.demoaut.com"
    wait_time = constant(2)

    # Note there is no @task decorator. If we decorate it that way, it will be picked up randomly just like any other
    # task
    def on_start(self):
        print("Logging in....")

    @task
    def doing_work(self):
        print("Doing work....")

    # Note there is no @task decorator.
    def on_stop(self):
        print("Logging out...")
