import collections

from types import MappingProxyType


d = {
    "name": "Charlie",
    "age": 28,
    "city": "Austin",
    "occupation": "Engineer",
    "salary": 87000,
    "experience": 5,
    "remote": True
}

# This will error because state is missing
# print(d["state"])

# This will not error
print(d.get("state", "State Unknown"))

# This will also not error
defaultD = collections.defaultdict(lambda: "State Unknown")
defaultD |= d
print(defaultD["state"])



# Trying to change a proxy is not allowed
proxyD = MappingProxyType(d)
# proxyD["age"] = 23



