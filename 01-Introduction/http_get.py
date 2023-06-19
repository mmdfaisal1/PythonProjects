from locust import HttpUser, constant, task


class MyHttpUser(HttpUser):
    host = "http://resreq.in"
    wait_time = constant(2)

    # @task
    # def launch_url(self):
    #     response = self.client.get("/api/users")
    #     print(response.text)

    @task
    def create_user(self):
        payload = {
            "name": "faisal",
            "job": "test engineer"
        }
        response2 = self.client.post("/api/users", json=payload)
        print(response2.text)
