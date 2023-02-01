import re


match = re.search(r'iii', 'piiig')  # found, match.group() == "iii"
match = re.search(r'igs', 'piiig')  # not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig')  # found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'abc123def')  # found, match.group() == "123"
match = re.search(r'\w\w\w', '123abc456')  # found, match.group() == "abc"
