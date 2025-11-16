---
title: "Python Data Model"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
---

These are my notes on the first chapter of Fluent Python by Luciano Romalho.

# Special Methods

Special methods are those double underscore methods you see in python all the time.

Using these special methods helps take the guesswork out of people using your class. For example, `__getitem__` allows users to use `[]` to get an item from your object!

Using special methods like this also allows for implicit calls, such as when `for i in x` implicitly calls `__iter__`. Also this allows for some of the more primitive classes written in C to use more optimized code. In fact, with the exception of `__init__`, most of your calls to these special methods should be implicit.

## Mathematical Special Methods

There's methods like `__add__` that can allow you to use `a + b` to implicitly call that function to `a` and `b`.

## String Special Methods

There are two special string methods: `__repr__` and `__str__`. 

`__repr__` is the debugger's string representation. You can also call this using `!r` in a formatted string.

`__str__` is the user-friendly string for `str()`. You can also call this using `!s` in a formatted string.

If `__repr__` is also a user-friendly string, leave `__str__` empty and `str()` will call `__repr__` as fallback. 

## Boolean Special Method

Implement `__bool__` if you want your object to act as a boolean. If unimplemented, it tries to return `__len__() != 0` instead.

# Mini Mini Project

See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython1.py) for a couple classes I made that use some of the above special methods. The `Date` class implements `__add__` and `__repr__`. The `MonthData` class is a dumb way of storing some info about each month for use by the `Date` class, but I wanted to build it to try using the `__getitem__` method.



