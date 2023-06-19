from locust import task, TaskSet, constant, User


class UserBehavior(TaskSet):
    wait_time = constant(10)

    @task(1)
    class CartModule(TaskSet):
        @task(8)
        def add_to_cart(self):
            print("I am adding to cart")

        @task(4)
        def delete_from_cart(self):
            print("I am deleting from cart")

        @task(1)
        def stop_method(self):
            print("I am stopping Cart Module")
            # reschedule=False mean that that this class, Car Module, won't be immediately scheduled again
            # It will be rescheduled based on on the wait_time in the parent class, User Behavior
            self.interrupt(reschedule=False)

    @task(3)
    class ProductModule(TaskSet):
        @task(8)
        def view_product(self):
            print("I am viewing product")

        @task(4)
        def buy_product(self):
            print("I am buying product")

        @task(1)
        def stop_method(self):
            print("I am stopping Product Module")
            self.interrupt(reschedule=False)


class MyUser(User):
    wait_time = constant(2)
    tasks = [UserBehavior]
