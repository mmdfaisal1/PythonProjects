from locust import HttpUser, constant, task, SequentialTaskSet
from locust.exception import StopUser


class UserBehavior(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.jsession_id: str = ""

    def on_start(self):
        print("I am launching URL")
        response = self.client.get("/InsuranceWebExtJS/index.jsf", name="LaunchURL")
        self.jsession_id = response.cookies["JSESSIONID"]
        print(self.jsession_id)

    @task
    def select_auto_quote(self):
        print("I am selecting auto quote, using jsession_id: ", self.jsession_id)
        cookies_to_send = {"JSESSIONID": self.jsession_id}  # this is a dictionary
        # cookies parameter accepts a dictionary
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf", cookies=cookies_to_send,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Did not receive 200 status code")
        raise StopUser()


class MyUser(HttpUser):

    host = "http://demo.borland.com"
    wait_time = constant(4)
    tasks = [UserBehavior]


