import re

# Open file
file = open('/home/ivan/education-python/regular-expressions/file.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
emails = re.findall(r'[\w.-]+@[\w.-]+', file.read())

for email in emails:
    print(email)
