from threading import RLock, Lock, Thread


class ChopStick:
    def __init__(self, number):
        self.lock = Lock()
        self.name = number

    def pick_up(self):
        return self.lock.acquire(timeout=0.1)

    def put_down(self):
        self.lock.release()


class Philosopher:
    def __init__(self, left_stick, right_stick, common):
        self.left = left_stick
        self.right = right_stick
        self.c = common
        self.bites = 10

    def pick_up(self):
        if self.left.pick_up():
            if self.right.pick_up():
                return True
            else:
                self.left.put_down()
        return False

    def put_down(self):
        self.right.put_down()
        self.left.put_down()

    def chew(self):
        self.c.append('chew')
        print("chew")
        self.bites -= 1

    def eat(self):
        if self.pick_up():
            self.chew()
            self.put_down()

    def run(self):
        while self.bites > 0:
            self.eat()

common = []

c0 = ChopStick(0)
c1 = ChopStick(1)
c2 = ChopStick(2)
c3 = ChopStick(3)
c4 = ChopStick(4)

p0 = Philosopher(c0, c1, common)
p1 = Philosopher(c1, c2, common)
p2 = Philosopher(c2, c3, common)
p3 = Philosopher(c3, c4, common)
p4 = Philosopher(c4, c0, common)

thread_0 = Thread(target=p0.run)
thread_1 = Thread(target=p1.run)
thread_2 = Thread(target=p2.run)
thread_3 = Thread(target=p3.run)
thread_4 = Thread(target=p4.run)

for thread in (thread_0, thread_1, thread_2, thread_3, thread_4):
    thread.start()

for thread in (thread_0, thread_1, thread_2, thread_3, thread_4):
    thread.join()
print("End")
print(len(common))
