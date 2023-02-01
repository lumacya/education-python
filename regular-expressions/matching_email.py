import re

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)

if match:
    print(f"found: {match.group()}")
else:
    print('did not find')

# В этом случае поиск не дает полного адреса электронной почты, потому что \w не совпадает с '-' или '.' в адресе.

match = re.search(r'[\w.-]+@[\w.-]+', str)
# Квадратные скобки можно использовать для обозначения набора символов, поэтому [abc] соответствует 'a' или 'b' или 'c'. Коды \ w, \ s и т. Д. также работают внутри квадратных скобок, за одним исключением, что точка (.) просто означает буквальную точку.

if match:
    print(f"found: {match.group()}")
else:
    print('did not find')
