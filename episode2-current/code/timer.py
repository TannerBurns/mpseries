import time

from typing import NamedTuple, Any, Callable

class TimerResponse(NamedTuple):
    elapsed: float
    results: Any

class Timer(object):
    
    def run(self, fn: Callable, *args: list, **kwargs: dict) -> TimerResponse:
        self.start_time = time.time()
        results = fn(*args, **kwargs)
        self.stop_time = time.time()
        self.elapsed = self.start_time - self.stop_time
        return TimerResponse(self.elapsed, results)