import threading
import time


def alice():
    while True:
        time.sleep(5)
        print("This is Alice")


def bob():
    while True:
        time.sleep(1)
        print("This is Bob")


threading.Thread(target=alice).start()
threading.Thread(target=bob).start()
