import time
from concurrent.futures import ThreadPoolExecutor


def a():
    while True:
        print("a")
        time.sleep(1)

def b():
    while True:
        print("b")
        time.sleep(1.2)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(a)
    executor.submit(b)
