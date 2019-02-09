from threading import Thread, Condition
from time import sleep

number = 0
fizz_checked = False
buzz_checked = False
fizzbuzz_checked = False


def fizz(cond: Condition):
    global fizz_checked
    for _ in range(100):
        with cond:
            print("f")
            cond.wait()
            print("ff")
            if number % 3 == 0 and number % 15:
                print("fizz")
            fizz_checked = True
            print("fff")
            cond.notify_all()
            if number > 100:
                return


def buzz(cond: Condition):
    global buzz_checked
    for _ in range(100):
        with cond:
            print("b")
            cond.wait()
            print("bb")
            if number % 5 == 0 and number % 15:
                print("buzz")
            buzz_checked = True
            print("bbb")
            cond.notify_all()
        if number > 100:
            return


def fizzbuzz(cond: Condition):
    global fizzbuzz_checked
    for _ in range(100):
        with cond:
            print("fb")
            cond.wait()
            print("fbfb")
            if number % 15 == 0:
                print("fizzbuzz")
            fizzbuzz_checked = True
            cond.notify_all()
        sleep(0.1)
        if number >= 100:
            print("end")
            return


def checked_all():
    print("checked0")
    print(fizz_checked)
    print(buzz_checked)
    print(fizzbuzz_checked)
    print("checked1")
    return fizz_checked and buzz_checked and fizzbuzz_checked


def num(cond: Condition):
    global number, fizzbuzz_checked, buzz_checked, fizz_checked
    for _ in range(200):
        with cond:
            number += 1
            print("num: " + str(number))
            fizzbuzz_checked = False
            buzz_checked = False
            fizz_checked = False
            cond.notify_all()
            print("num")
            cond.wait_for(checked_all, timeout=10)
            print("numnum")
        if number >= 100:
            print("num end")
            return


if __name__ == '__main__':
    cond = Condition()

    fizz_thread = Thread(target=fizz, args=(cond,))
    buzz_thread = Thread(target=buzz, args=(cond,))
    fizzbuzz_thread = Thread(target=fizzbuzz, args=(cond,))
    number_thread = Thread(target=num, args=(cond,))

    fizz_thread.start()
    buzz_thread.start()
    fizzbuzz_thread.start()

    sleep(1)
    number_thread.start()

    fizz_thread.join()
    buzz_thread.join()
    fizzbuzz_thread.join()
    number_thread.join()

