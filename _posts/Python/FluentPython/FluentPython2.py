example_data = [
    ("Alice", 28, "Engineer", "New York"),
    ("Bob", 35, "Designer"),
    ("Charlie", 42, "Engineer", "San Francisco", "CA"),
    ("Diana", 31, "Developer", "Austin"),
    ("Eve", 29, "Analyst", "Boston", "MA", "USA"),
    ("Frank", 45, "Engineer"),
    ("Grace", 33, "Consultant", "Seattle", "WA"),
    ("Henry", 38, "Architect", "Portland"),
    ("Iris", 27, "Researcher", "Portland", "OR", "USA"),
    ("Jack", 40, "Administrator")
]

for x in example_data:
    match x:
        case (name, _, 'Engineer', *_):
            print(f'{name} is an Engineer')
        case (name, _, _, "Portland", *_):
            print(f'{name} is from Portland')