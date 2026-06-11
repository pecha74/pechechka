#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()


f = open(r'C:/Users/User/OneDrive/Рабочий стол/Python/repo/Homework/text.txt', "w+t")
f.write("Hello\n")

f.seek(0)

content = f.read

print(content, end='')
f.close()