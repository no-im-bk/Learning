---
title: "Python References"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
---

These are my notes on Chapter 6 of Fluent Python by Luciano Ramalho.

# References

In python, variables are actually references to objects.

You can use `==` to compare if the contents of objects are equal, but `is` compares if the references themselves are the same.

You can use `id` to see the id of the object the variable is referencing.

## Copying

Copying mutable objects using their constructor is shallow by default. The `copy` module has a `copy()` method for shallow copies and a `deepcopy()` method for deep copies.

You can control how a copy happens via the copy module by implementing `__copy__` or `__deepcopy__`.

Copying an immutable object creates a reference to the same object.

## Functions

Functions in python are pass by reference. Because of this, you need to be aware of if the function you are writing is changing a mutable parameter in it!

Mutable types used as default params are shared!

## Garbage collection

Each object has a counter with the number of references pointing to it. This is decremented at the end of scope. You can also use `del` to manually delete a reference (but not the object).

See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython6-1.py) for some code involving references.

