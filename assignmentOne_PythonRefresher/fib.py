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
    csvName = f"assignmentOne_PythonRefresher/{func.__name__}TimeLog.csv"

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


"""
Output when function is run:

Finished in 0.00000000s: f(0) -> 0
Finished in 0.00000000s: f(1) -> 1   
Finished in 0.00100088s: f(2) -> 1   
Finished in 0.00000000s: f(3) -> 2   
Finished in 0.00200176s: f(4) -> 3   
Finished in 0.00099874s: f(5) -> 5   
Finished in 0.00300050s: f(6) -> 8   
Finished in 0.00000000s: f(7) -> 13  
Finished in 0.00399995s: f(8) -> 21  
Finished in 0.00000000s: f(9) -> 34  
Finished in 0.00399995s: f(10) -> 55 
...
Finished in 0.00000000s: f(95) -> 31940434634990099905
Finished in 0.04300117s: f(96) -> 51680708854858323072
Finished in 0.00000000s: f(97) -> 83621143489848422977
Finished in 0.04300117s: f(98) -> 135301852344706746049
Finished in 0.00000000s: f(99) -> 218922995834555169026
Finished in 0.04400110s: f(100) -> 354224848179261915075
"""