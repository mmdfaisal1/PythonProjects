def function1():
    print("Hi I am function1")


def function2(func):
    print("Hi I am function2\nNow I will call function1")
    func()


function2(function1)

