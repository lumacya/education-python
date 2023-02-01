import re

# Open file
file = open('file.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
emails = re.findall(r'[\w.-]+@[\w.-]+', file.read())
