---
title: "Python Functions"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
---

These are my notes on Chapter 7 of Fluent Python by Luciano Ramalho.

Functions are Objects!

Functions can contain docstrings in triple quotes that can be accessed via `help()` or `__doc__()`.

```python
def really_cool_function():
    """This is the coolest docstring EVER!!!!"""
    print("haiiiiiii")
    return 67
```

`map`, `reduce`, and `filter` are offered in Python. `map` and `filter` are built-in but list comprehension already does what those do. `reduce` is available in `functools`.

`lambda` can be used to create anonymous functions:
```python
cool_function = lambda x, y: x * y
```

You can make an object callable with `__call__`.

# Parameters

Since 3.8, parameters before a `/` are positional only and cannot be called with the name of the param. I.e: `def add(a,b,/)` cannot be called as `add(a=1,b=2)` but must be called as `def add(1,2)`.

Parameters after a `*` or after a param with a `*` MUST be called with their param names.

A param with a `*` catches extra arguments as a tuple. A param with a `**` catches extra arguments as a dict.

# Functional Programming tidbits

The `operator` package contains a lot of math functions, a `itemgetter`, a `attrgetter` and a `methodcaller`.

`functools` has a `partial` function that can return a function from an existing function but with some of the params already filled in:
```python
add_two = functools.partial(add, 2)
```

See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython7-1.py) for some code involving functional programming.
