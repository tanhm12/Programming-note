import re

# https://developers.google.com/edu/python/regular-expressionshttps://developers.google.com/edu/python/regular-expressions

text = 'test text'

# Removing occurence at the start 
re.sub(r'^some text', '', text)

# Removing occurence at the end 
re.sub(r'some text$', '', text)

# Handling all date formats
re.sub(r'\d+[\.\/-]\d+[\.\/-]\d+', '', 'Today is 14-07-2021')
re.sub(r'\d+[\.\/-]\d+[\.\/-]\d+', '', 'Today is 14/07/2021')
re.sub(r'\d+[\.\/-]\d+[\.\/-]\d+', '', 'Today is 14.07.2021')

# remove url 
