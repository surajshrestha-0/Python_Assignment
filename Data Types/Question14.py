"""
Write a Python function to create the HTML string with tags around the word(s).
"""


def add_tag(tag, tag_element):
    return "<{}>{}<{}>".format(tag, tag_element, tag)


print(add_tag('i', 'Python'))
print(add_tag('b', 'Python Tutorial'))
