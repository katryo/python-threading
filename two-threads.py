import time
from threading import Thread

def a():
    for _ in range(5):
        print("a")
        time.sleep(1)

def b():
    for _ in range(5):
        print("b")
        time.sleep(1.2)


if __name__ == "__main__":
    thread_a = Thread(target=a)
    thread_b = Thread(target=b)

    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    print("fin")
