from typing import Dict
from typing import Generator
from functools import lru_cache

memo: Dict[int, int] = {0:0, 1:1}

def fib(n: int):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

def memoization_fib(n: int):
    if n not in memo:
        memo[n] = memoization_fib(n - 1) + memoization_fib(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def automatic_memoization_fib(n: int):
    if n < 2:
        return n
    return automatic_memoization_fib(n - 2) + automatic_memoization_fib(n - 1)

# Recusrive solutions can be solved iteratively as well 
def iterative_fib(n: int):
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def iterative_full_fib(n: int) -> Generator[int, None, None]:
    yield 0
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    yield  next