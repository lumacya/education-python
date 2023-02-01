# Предположим, что для проблемы с электронными письмами мы хотим извлечь имя пользователя и хост отдельно. Для этого добавьте круглые скобки ( ) вокруг имени пользователя и хоста в шаблоне, например: r'([\w.-]+)@([\w.-]+)'. В этом случае скобки не меняют то, чему будет соответствовать шаблон, вместо этого они устанавливают логические "группы" внутри текста соответствия. При успешном поиске match.group(1) - это текст соответствия, соответствующий 1-й левой круглой скобке, а match.group(2) - текст, соответствующий 2-й левой круглой скобке. Обычный match.group() по-прежнему представляет собой весь текст соответствия, как обычно.

import re


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)

if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
