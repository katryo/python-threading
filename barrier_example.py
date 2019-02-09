from threading import Barrier, Thread
from datetime import datetime
from time import sleep


class Runner:
    def run(self, barrier: Barrier):
        print("wait")
        barrier.wait()
        print("go")

        # for _ in range(3):
        #     print(datetime.now())
        #     sleep(1)


if __name__ == '__main__':
    barrier = Barrier(3)
    runner = Runner()

    thread_a = Thread(target=runner.run, args=(barrier,))
    thread_b = Thread(target=runner.run, args=(barrier,))
    thread_c = Thread(target=runner.run, args=(barrier,))

    thread_a.start()
    sleep(1)
    thread_b.start()
    sleep(1)

    thread_c.start()
