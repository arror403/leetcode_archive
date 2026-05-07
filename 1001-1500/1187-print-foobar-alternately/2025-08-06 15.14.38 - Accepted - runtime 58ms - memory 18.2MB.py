import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        # initially neither thread has access to bar
        self.bar_lock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_lock.acquire() # pick up foo lock
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release() # release bar lock so self.bar() can run


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_lock.acquire() # pick up bar lock
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release() # release foo lock so self.foo() can run again