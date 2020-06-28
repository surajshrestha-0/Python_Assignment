"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]', 'Python') -> [[Python]]
insert_sting_middle('<<>>', 'Python') -> <<Python>>
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""


def insert_sting_middle(bracket, text):
    return bracket[:2] + text + bracket[2:]


print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('<<>>', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
