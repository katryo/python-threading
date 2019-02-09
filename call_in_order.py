from threading import Thread, RLock, Semaphore

class Runner:
    def __init__(self, sem_a, sem_b):
        self.sem_0 = sem_a
        self.sem_1 = sem_b

        self.sem_0.acquire()
        self.sem_1.acquire()

    def first(self):
        self.sem_0.release()
        print("first")

    def second(self):
        self.sem_0.acquire()
        print("second 0")
        self.sem_0.release()
        print("second 1")
        self.sem_1.release()

    def third(self):
        self.sem_1.acquire()
        print("third")


class BadRunner:
    def __init__(self, locka:RLock, lockb:RLock):
        self.lock_a = locka
        self.lock_b = lockb

        self.lock_a.acquire()
        self.lock_b.acquire()

    def first(self):
        self.lock_a.release()
        print("first")

    def second(self):
        self.lock_a.acquire()
        print("second 0")
        self.lock_a.release()
        print("second 1")
        self.lock_b.release()

    def third(self):
        self.lock_b.acquire()
        print("third")


if __name__ == '__main__':
    # sem_a = Semaphore()
    # sem_b = Semaphore()
    # runner = Runner(sem_a, sem_b)
    #
    # thread_a = Thread(target=runner.first)
    # thread_b = Thread(target=runner.second)
    # thread_c = Thread(target=runner.third)
    #
    # thread_a.start()
    # thread_b.start()
    # thread_c.start()


    lock_a = RLock()
    lock_b = RLock()
    bad_runner = BadRunner(lock_a, lock_b)

    thread_a = Thread(target=bad_runner.first)
    thread_b = Thread(target=bad_runner.second)
    thread_c = Thread(target=bad_runner.third)

    thread_a.start()
    thread_b.start()
    thread_c.start()
