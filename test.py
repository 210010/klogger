from klogger import task, debug, info, log, progress_task, tick_progress
import klogger
from multiprocessing.pool import ThreadPool
import time

@debug
def foo(n):
    if n < 0:
        return

    foo(n - 1)

@progress_task(max_value=10)
def bar():
    for i in range(10):
        tick_progress(amount=3)
        time.sleep(0.1)

def test_recursion():
    pool = ThreadPool(4)
    def work(n):
        foo(n)

    r = []
    for i in range(10):
        r.append(pool.apply_async(foo, args=(i, )))

    for a in r:
        a.get()

def test_progress():
    pool = ThreadPool(10)

    r = []
    for i in range(10):
        r.append(pool.apply_async(bar))

    for a in r:
        a.get()

def main():
    test_progress()

if __name__ == "__main__":
    klogger.set_verbosity(klogger.DEBUG)
    main()