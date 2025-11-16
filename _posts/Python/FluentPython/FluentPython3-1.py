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
    },
    {
        "age": 24,
        "city": "Seattle"
    }
]

for d in dicts:
    match d:
        case {"occupation": "Engineer", "name": name}:
            print(f"{name} is an Engineer.")
        case {"remote": True, "name": name}:
            print(f"{name} is not an engineer but is remote.")
        case {"name": name}:
            print(f"{name} is neither an Engineer or remote.")
        case _:
            print(f"Invalid data: {d!r}")