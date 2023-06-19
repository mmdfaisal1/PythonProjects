import json
from types import SimpleNamespace
from locust import task, HttpUser, constant


class MyResReq(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(3)

    @task
    def get_users(self):
        response = self.client.get("/api/users")
        print(response.status_code)

        # json_object: dict = json.loads(response.text)
        # print(json_object['total'])
        # data_list: list = json_object['data']
        # print(data_list[0])
        # first_id = data_list[0]['id']
        # print("The first id is:", first_id)

        # json_string = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        # json_object: dict = json.loads(json_string)
        # print(json_object['hometown'])
        # print(json_object['hometown']['name'])

        # json_data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        # my_object = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))
        # print(my_object.hometown.name)
        # print(type(my_object))

    @task
    def create_user(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.client.post("/api/users", json=payload)
        print(response.status_code)
        print(response.text)




