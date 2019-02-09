from threading import Condition, Thread
from datetime import datetime
from time import sleep

class Runner:
    def run(self, cond):
        with cond:
            cond.wait()
            print(datetime.now())

    def notify(self, cond):
        with cond:
            sleep(3)
            print("notify")
            cond.notify_all()


if __name__ == '__main__':
    cond = Condition()
    runner = Runner()

    thread_a = Thread(target=runner.run, args=(cond,))
    thread_b = Thread(target=runner.run, args=(cond,))
    thread_c = Thread(target=runner.notify, args=(cond,))

    thread_a.start()
    thread_b.start()
    thread_c.start()
