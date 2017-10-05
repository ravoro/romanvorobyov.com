title: Memoization (and Python's lru_cache)

<header id="article-header" markdown="1">
This article is a brief on memoization and how it can be achieved using Python's
[lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache){target="_blank"}
decorator.
</header>

Memoization is an optimization technique that caches a function's results based on input value.

Given an initially unique input the result is calculated and cached,
such that any subsequent calls with the same input return the initial cached result
(instead of performing a recalculation).

Memoization is a *time-memory tradeoff*
(i.e. subsequent computation time is saved at the cost of keeping initial calculated results in memory)

Memoization is useful for pure functions (that always return the same result for the same input),
whose results can be cached without a concern that they may be out of date.

Python 3.2+ provides an simple memoization solution in the form of the
[lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache){target="_blank"}
decorator.

For example, a memoized solution for computing the Fibonacci sequence simply requires the addition of the @lru_cache decorator.

```
@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
```

<footer id="article-footer" markdown="1">  
**P.S.**

For more details on memoization:

- [Memoization in Python](https://mike.place/2016/memoization/){target="_blank"}
  by Mike Lee Williams.
- [Мемоизация и каррирование (Python)](https://habrahabr.ru/post/335866/){target="_blank"}
  by German Gorelkin.

For more details on Python's lru_cache decorator:

- [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache){target="_blank"}
  section of Python documentation.
</footer>
