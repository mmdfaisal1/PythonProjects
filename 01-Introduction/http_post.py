from locust import HttpUser, constant, task


class MyHttpUser(HttpUser):

    host = "http://resreq.in"
    wait_time = constant(4)

    @task
    def create_user(self):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "name": "faisal",
            "job": "test engineer"
        }
        # res1 = self.client.post("/api/users", headers=headers, data=payload)
        # res1 = self.client.post("/api/users", json=payload)
        res1 = self.client.get("/api/users")

        print(res1.status_code)
        print(res1.text)


# if __name__ == "__main__":
#     from locust.env import Environment
#     my_env = Environment(user_classes=[MyHttpUser])
#     MyHttpUser(my_env).run()
