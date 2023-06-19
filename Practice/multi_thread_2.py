import threading
from time import sleep

counter = 0


def func1():
    global counter

    while True:
        counter += 1
        counter -= 1
        # sleep(5)
        # print("Value of counter in func1:", counter)


def func2():
    global counter

    while True:
        counter += 1
        counter -= 1
        # sleep(5)
        # print("Value of counter in func2:", counter)


threading.Thread(target=func1).start()
threading.Thread(target=func2).start()
while True:
    print("Value of counter is:", counter)
    sleep(2)









