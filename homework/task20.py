#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt:

# выходные данные:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

with open (r'C:/Users/User/OneDrive/Рабочий стол/Python/repo/Homework/import_this.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end='')