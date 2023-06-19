from time import sleep

from locust import HttpUser, constant, task, SequentialTaskSet
import logging

# __name__ means name of the module itself
# https://docs.python.org/3/howto/logging.html
from locust.exception import StopUser

logger = logging.getLogger(__name__)


class MySequentialTaskSet(SequentialTaskSet):

    @task
    def get_user(self):
        self.client.request()
        with self.client.get("/get", name="API Get Method", catch_response=True) as response:
            if "73" in response.text:
                response.success()
                print("Success")
                logger.info("The required text found in response")

            else:
                response.failure("Could not find the required text")
                logger.error("Exiting the test run")
                # The following exits the test runner
                self.parent.environment.runner.quit()

    # @task
    # def create_user(self):
    #     payload = {
    #         "name": "faisal",
    #     }
    #     response = self.client.post("/post", json=payload)
    #     print(response.text)


class MyHttpUser(HttpUser):
    # Reading the below from locust.conf file
    host = "https://httpbin.org"
    wait_time = constant(4)
    tasks = [MySequentialTaskSet]


