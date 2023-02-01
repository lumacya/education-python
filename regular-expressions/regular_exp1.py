import re  # модуль для работы с регулярными выражениями

# В Python поиск по регулярным выражениям обычно записывается как:
# match = re.search(pattern, string)
str = "an example word:cat!!"
match = re.search(r"word:\w\w\w", str)

# оператор if, чтобы проверить, был ли поиск успешным
if match:
    print(f"Found {match.group()}")
else:
    print("Did not find")
