from functools import lru_cache
from time import time
import csv


def timer(func):
    def wrap_func(args):
        startTime = time()
        result = func(args)
        endTime = time()
        timeDelta = endTime - startTime

        print(f"Finished in {(timeDelta):.8f}s: f({args}) -> {result}")
        return result

    return wrap_func


def time_logger(func):
    # This is an additional decorator that I created so that I can log the execution time of a function directly to a csv, rather than just crudely adding the functionality to the timer decorator.
    csvName = f"{func.__name__}TimeLog.csv"

    with open(csvName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["input", "executionTime"])

    def wrap_func(args):
        startTime = time()
        result = func(args)
        endTime = time()
        timeDelta = endTime - startTime

        with open(csvName, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([args, f"{(timeDelta):.8f}"])
        return result

    return wrap_func


@lru_cache
@timer
@time_logger
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    fib(100)
