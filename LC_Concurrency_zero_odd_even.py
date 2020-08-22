from threading import Event as e
from threading import Thread as t

from sys import stdin as si

class ZeroEvenOdd:
    def __init__(self, nu):
        self.n = nu
        self.i = 0
        self.zero = e()
        self.odd = e()
        self.even = e()
        self.zero.set()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        self.zero.wait()
        printNumber(self.i)
        self.zero.clear()
        if self.i % 2 == 0:
            self.odd.set()
        else:
            self.even.set()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        self.even.wait()
        printNumber(self.i)
        self.i += 1
        self.even.clear()
        self.zero.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        self.odd.wait()
        printNumber(self.i)
        self.i += 1
        self.odd.clear()
        self.zero.set()


global num


def printNumber(x):
    num += str(x)


def spawn_zero(z, nu: int):
    for i in range(nu):
        z(printNumber)


def spawn_num(z, nu: int):
    for i in range(nu//2):
        z(printNumber)


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        num = ''
        n = int(si.readline().strip())
        zoe = ZeroEvenOdd(n)
        t1 = t(target=spawn_zero, args=(zoe.zero, n))
        t2 = t(target=spawn_num, args=(zoe.odd, n))
        t3 = t(target=spawn_num, args=(zoe.even, n))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()