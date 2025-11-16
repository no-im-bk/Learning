---
title: "Python Unicode Text"
categories:
  - Learning
tags:
  - Fluent Python
  - Python
  - Unicode
---

These are my notes on Chapter 4 of Fluent Python by Luciano Ramalho.

# Characters

Characters in python follow the Unicode standard.

They can be encoded into bytes using a variety of encoding methods.

For example, `A` is unicode `U+0041` which is encoded into `\x41` when we encode it into UTF-8. But it could also get encoded as `'\x41\x00` with UTF-16LE.

You can represent an encoded string as `bytes` (immutable) or `bytearray` (mutable)

When trying to encode or decode bytes, you can get `UnicodeEncodeError` or `UnicodeDecodeError` if a character or byte array is invalid.

To handle the decode errors, you could use decode as follows:

```python
octets.decode('utf_8', errors='replace')
```

## Normalizing unicode text

`unicodedata.normalize` can normalize text for easier comparison since different unicode combinations can render the same characters. The `NFC` and `NFD` options normalize the same looking characters to the same unicode, while `NFKC` and `NFKD` are stricter and also do similar looking characters (like greek mu and mathematical mu). The `NFD` and `NFKD` also make combining characters be separate.

`casefold()` converts uppercase to lowercase.


## Sorting unicode text

Using `sorted()` doesn't work because the order of unicode characters doesn't reflect real life language sorting rules, and these can vary based on language.

`pyuca` is a library made to solve this problem.


## Unicode database

Unicode actually has a big database with a bunch of metadata on each character that can be access with methods such as `name()` and `numeric()`.

## Other notes

The `re` module treats `bytes` as ASCII but `str` normally as unicode.

The `os` module encodes all filename and pathname arguments using `sys.getfilesystemencoding()` since most terminals don't support unicode.

See [here](https://github.com/no-im-bk/Learning/blob/master/_posts/Python/FluentPython/FluentPython4-1.py) for an example of how to remove combining marks and how the default sorting in python screws up with unicode characters.