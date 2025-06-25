from threading import Semaphore, Thread

class Foo:
    def __init__(self):
        self.first_lock = Semaphore(0)
        self.second_lock = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print("inside first")
        printFirst()
        self.first_lock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        print("inside second")
        with self.first_lock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        print("inside third")
        with self.second_lock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


def printFirst():
    print("first", end='')

def printSecond():
    print("second", end='')

def printThird():
    print("third", end='')


foo = Foo()

# Simulating threads being started in random order
t1 = Thread(target=foo.first, args=(printFirst,))
t2 = Thread(target=foo.second, args=(printSecond,))
t3 = Thread(target=foo.third, args=(printThird,))

# Start in a shuffled order
t3.start()
t2.start()
t1.start()

# Wait for all to finish
t1.join()
t2.join()
t3.join()