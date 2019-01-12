import re


lorem = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Quisque a sapien eleifend, lacinia dui vitae, rhoncus dui.
Aenean tristique enim sit amet ligula malesuada, quis porta ante cursus.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
lorem_words_strip = re.sub('(\n|,|\.)', '', lorem)
lorem_words = lorem_words_strip.split(' ')
