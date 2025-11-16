import copy
print("Create two lists with same elements")
a = [1, 2, [3]]
b = [1, 2, [3]]

print("Check if elements are the same")
print(a == b)
print("Create if the reference is the same")
print(a is b)

print("Make a copy of a and add an element to a")
b = copy.copy(a)
a[-1].append(4)
print(f"a: {a}")
print(f"b: {b}")

print("Make a deep copy of a and add an element to a")
b = copy.deepcopy(a)
a[-1].append(4)
print(f"a: {a}")
print(f"b: {b}")

print("Show pass by reference by adding an element inside a function")
def addfive(arr):
    arr.append(5)

addfive(a)
print(a)

print("Create two tuples with same elements")
c = (1, 2, 3)
d = (1, 2, 3)

print("Check if elements are the same")
print(c == d)
print("Create if the reference is the same")
print(c is d)

print("Make a copy of a and see if it points to same object")
c = copy.copy(d)
print(c is d)