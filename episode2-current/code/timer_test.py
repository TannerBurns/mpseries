import time

from typing import NamedTuple, Any, Callable


class TimerResponse(NamedTuple):
    elapsed: float
    results: Any


class Timer(object):
    def __init__(self):
        self.start = 0
        self.stop = 0
        self.elapsed = 0
    
    def run(self, fn: Callable, *args: list, **kwargs: dict):
        self.start = time.time()
        results = fn(*args, **kwargs)
        self.stop = time.time()
        self.elapsed = self.start - self.stop
        return TimerResponse(self.elapsed, results)
            

'''
def test():
    def add(x, y):
        return x+y

    timer = Timer()
    tresp = timer.run(add, 1, 2)
    print(tresp)

if __name__ == '__main__':
    test()
'''