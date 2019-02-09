from threading import Semaphore, Thread
from datetime import datetime
from time import sleep


class Runner:
    def run(self, sem):
        for _ in range(3):
            with sem:
                print(datetime.now())
                sleep(1)


if __name__ == '__main__':
    sem = Semaphore(2)
    runner = Runner()

    thread_a = Thread(target=runner.run, args=(sem,))
    thread_b = Thread(target=runner.run, args=(sem,))
    thread_c = Thread(target=runner.run, args=(sem,))

    thread_a.start()
    thread_b.start()
    thread_c.start()
