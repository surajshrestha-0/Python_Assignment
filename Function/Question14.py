"""
Write a Python program to sort a list of dictionaries using Lambda.
"""


def sortDictionaries(input_tuple):
    return sorted(input_tuple, key=lambda x: x['salary'])


dicts = [
    {"name": "Ram", "salary": 10000},
    {"name": "Hari", "salary": 30000},
    {"name": "Shyam", "salary": 15000},
    {"name": "Gaurav", "salary": 20000}
]

print(sorted(dicts, key=lambda item: item['salary']))
