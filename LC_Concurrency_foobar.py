from threading import Event as e


class FooBar:
    def __init__(self, n):
        self.n = n
        self.e1 = e()
        self.e2 = e()
        self.e1.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.e1.wait()
            printFoo()
            self.e1.clear()
            self.e2.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.e2.wait()
            printBar()
            self.e2.clear()
            self.e1.set()

'''
https://leetcode.com/problems/print-foobar-alternately/
'''