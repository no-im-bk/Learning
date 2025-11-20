dicts = [
    {
        "name": "Alice",
        "age": 28,
        "city": "New York",
        "occupation": "Engineer",
        "salary": 95000
    },
    {
        "name": "Bob",
        "age": 34,
        "city": "San Francisco",
        "occupation": "Designer"
    },
    {
        "name": "Charlie",
        "age": 28,
        "city": "Austin",
        "occupation": "Engineer",
        "salary": 87000,
        "experience": 5,
        "remote": True
    },
    {
        "name": "Diana",
        "age": 41,
        "occupation": "Manager",
        "salary": 120000,
        "department": "Sales"
    },
    {
        "name": "Eve",
        "age": 29,
        "city": "Boston",
        "occupation": "Engineer"
    },
    {
        "name": "Frank",
        "age": 28,
        "city": "Seattle",
        "occupation": "Developer",
        "salary": 110000,
        "experience": 7,
        "remote": True,
        "skills": ["Python", "Java"]
    },
    {
        "name": "Grace",
        "age": 45,
        "city": "Denver",
        "occupation": "Designer",
        "salary": 78000
    },
    {
        "name": "Henry",
        "age": 52,
        "city": "Chicago",
        "occupation": "Manager",
        "department": "Engineering",
        "remote": False
    },
    {
        "name": "Iris",
        "age": 28,
        "occupation": "Engineer",
        "salary": 92000
    },
    {
        "name": "Jack",
        "age": 36,
        "city": "Portland",
        "occupation": "Designer",
        "salary": 85000,
        "experience": 10,
        "remote": True,
        "department": "Product"
    }
]

import operator
import functools

def people_sorter(dicts):
    """Sorts dicts based on age
    and prints the harmonic mean of their ages"""
    
    print("Sorted Names:")
    for person_data in sorted(dicts, key=operator.itemgetter("age")):
        print(person_data["name"])

    multiplicative_invert = functools.partial(operator.truediv,1)
    print("Harmonic mean of ages:")
    print(len(dicts) / functools.reduce(operator.add, (multiplicative_invert(d["age"]) for d in dicts)))
          
print(people_sorter.__doc__)

people_sorter(dicts)
    