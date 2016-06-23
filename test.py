from klogger import task, debug, info, log
import klogger
from multiprocessing.pool import ThreadPool

@debug
def foo(n):
    if n < 0:
        return

    foo(n - 1)

def main():
    pool = ThreadPool(4)
    def work(n):
        foo(n)

    r = []
    for i in range(10):
        r.append(pool.apply_async(foo, args=(i, )))

    for a in r:
        a.get()

if __name__ == "__main__":
    klogger.set_verbosity(klogger.DEBUG)
    main()