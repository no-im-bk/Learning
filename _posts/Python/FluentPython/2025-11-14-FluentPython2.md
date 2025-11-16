---
title: "Python Sequences"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
---

These are my notes on Chapter 2 of Fluent Python by Luciano Ramalho.

# Properties of sequences

Sequences can be categorized like so:

## Container sequences vs. Flat sequences

Container sequences hold items of different types. These are stored as references.
Flat sequences hold items of the same type. The actual value of the contents is stored. This makes flat sequences use less memory.

## Mutable vs. immutable

`list` is mutable while stuff like `tuple` and `str` are not.

Mutable sequences actually inherit from Immutable sequences.

# Lists

## List comprehension

Easy way to build a list from a list.

Ex: `[abs(x) for x in arr]`

You can filter the elements too:

`[abs(x) for x in arr if x % 2 == 0]`

You can also take the cartesian product of two lists:

`[(x, y) for x in x_coords for y in y_coords]`

## Generator expression

Similar syntax as list comprehension but it creates an iterator instead of a list, which avoids putting the whole list in memory:

`tuple(abs(x) for x in arr)`

# Tuples

The action of converting tuples to named variables is called unpacking:

`month, day = ("jan", 1)`

The references stored in a tuple are immutable but the actual data may be mutable.

Equivalence of tuples is based off of the values in it.

They are better performing than lists.

# Unpacking

Any sequence can be unpacked. The `*` prefix can unpack a sequence when used on the right side:

```python
>>> *range(3), 3
(0, 1, 2, 3)
```

When unpacking, the `*` prefix can collect extra items when used on the left side:
```python
>>> a, *rest = range(3)
(0, [1, 2])
```

# Pattern matching with sequences

The match case syntax allows you to match sequences and destructure to extract their info.

See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython2.py) for an example.

# Slices

Slices are technically objects. `a:b:c` generates `slice(a,b,c)`

# Sorting

Functions like `list.sort` that only change the receiver should return `None` always.

`list.sort` sorts in-place while `sorted()` creates a new list.

# Things that aren't lists

## Arrays

It's a packed array like in C. You can use `array.tofile` or `array.fromfile` to save or load the array as a binary file.

A `memoryview` can be used to get a slice of an array without copying anything.

Though if you are going to be doing difficult number crunching, you should use NumPy

## Deques

It's a stack and queue in one! (aka a linked list)
