from locust import task, TaskSet, constant, User


class UserBehavior(TaskSet):

    @task
    class CartModule(TaskSet):
        @task
        def add_to_cart(self):
            print("I am adding to cart")

        @task
        def delete_from_cart(self):
            print("I am deleting from cart")

    @task
    class ProductModule(TaskSet):
        @task
        def view_product(self):
            print("I am viewing product")

        @task
        def buy_product(self):
            print("I am buying product")


class MyUser(User):
    wait_time = constant(2)
    tasks = [UserBehavior]
