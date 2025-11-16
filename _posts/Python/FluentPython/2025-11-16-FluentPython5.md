---
title: "Python Data Class"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
---

These are my notes on Chapter 5 of Fluent Python by Luciano Ramalho.

# Data Classes

Data Classes are classes that just have fields and minimal logic. By using a Data Class, the `__init__`, `__repr__` and `__eq__` methods are already built automatically for you!

NOTE that the existence of a data class could indicate an issue with the architecture of the class if the "lack of logic" is really just due to the logic being spread across other classes.

There are three main options for creating data classes:

### collections.namedtuple

This data class can make a factory function that generates tuples with named elements.

### typing.NamedTuple

This does the same as above, but also allows for a type to be assigned to each element. You can also "subclass" this. (Quotes because its a metaclass.)

### @dataclass decorator

This decorator allows you to make your own Data Class. This can be mutable unlike the above options. To set it immutable, set `frozen=True`. If the options `eq=True, frozen=True`, then it will also generate a `__hash__` method.

## Field Options

When setting a field's defaults, make sure it isn't a mutable object (like a list) because its shared across all instances of the class!

Field options can help with stuff like this:

```python
list_of_names: list = field(default_factory=list)
```

Theres a bunch of other options such as `init` and `compare` if you want to remove the field from the `__init__` or from comparisons. (And many more)

## Post Init

There is a `__post_init__` that can be implemented for data classes that is run after `__init__` and is usually used for input validation.

## InitVar

Using `InitVar` marks a variable for use for initialization only, so that it won't be used as a field.

## Pattern Matching

Classes can also have their fields pattern matched!


See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython5-1.py) for an example of how to use the dataclass decorator.

