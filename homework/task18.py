#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

with open(r'C:\Users\ИВП-Сервис\Desktop\python\repo\homework\dump.txt', "r", encoding = 'UTF-8') as file:
    text = file.read()

text = text.lower()

letters = 'аеёиоуыэюяaeiouy'

dict = {}

for i in text:
    if i in letters:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

total = sum(dict.values())

print(f"Кол-во гласных букв в тексте: {total}")

for k, v in dict.items():
    print(f" {k} : {v}")

if total == 0:
    print("тут нет гласных")
