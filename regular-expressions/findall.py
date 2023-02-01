# findall(), вероятно, является самой мощной функцией в модуле re. Выше мы использовали re.search(), чтобы найти первое совпадение для шаблона. findall() находит все совпадения и возвращает их в виде списка строк, каждая строка представляет одно совпадение.

import re

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings

emails = re.findall(r'[\w.-]+@[\w.-]+', str)

for email in emails:
    print(email)
