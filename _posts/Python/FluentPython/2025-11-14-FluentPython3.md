---
title: "Python Dicts and Sets"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
---

These are my notes on Chapter 3 of Fluent Python by Luciano Ramalho.


# Dicts

Dicts can be unpacked with `**`

You can also use `|` to combine dicts. If the same key is used in both, the value of the right is used.

Pattern matching with `match case` works as well. See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython3-1.py) for an example.

## Handling missing values

If you want dict access without erroring out when a key doesn't exist, use `dict.get(key, default)`.

If you want dict access without erroring out when a key doesn't exist, AND want to add a new key when it doesn't exist use `dict.setdefault(key, default)`.

You can implement `__missing__` when you subclass stuff like dict or UserDict to do stuff if the key used is missing.

## Other cool dicts

Provide `DefaultDict` a callable on construction and if a key doesn't exist it will use the callable to generate a value and put the key value pair in the dict.

`OrderedDict` has ordered keys.

`ChainMap` is a sequence of dicts. Gets and sets access the first dict that has the matching key.

`Counter` takes in a sequence and turns it into a dict where the keys are the elements of the sequence and the values are the number of times they appear.

`UserDict` is what you should subclass in order to create your own dict as it is a version of dict that simplifies the coding of special methods.

`MappingProxyType` can make a copy of a dict that is read only.

See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython3-2.py) for an example using some of these dicts.

## dict views

`.keys()`, `.values()` and `.items()` return dynamically changing views of the dict. These are iterable and can be turned into lists, but are not lists themselves.

# Sets

They do a bunch of cool set operations like unions and intersections. `set` is mutable while `frozenset` is immutable. dict views are (almost) `frozenset`.