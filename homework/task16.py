# # todo: База данных пользователя.
# # Задан массив объектов пользователя


# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

# #Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

def format_age(age):
    # Возвращает правильное склонение слова 'год' для возраста
    if 11 <= age % 100 <= 19:
        return f"{age} лет"
    elif age % 10 == 1:
        return f"{age} год"
    elif 2 <= age % 10 <= 4:
        return f"{age} года"
    else:
        return f"{age} лет"

print("Выберите тип сортировки:")
print("1. По возрасту (больше введенного)")
print("2. По первой букве логина")
print("3. По группе")
choice = input("Тип сортировки: ").strip()

if choice == '1':
    try:
        age_limit = int(input("Введите минимальный возраст: "))
    except ValueError:
        print("Ошибка: возраст должен быть числом.")
        exit()
    filtered = [user for user in users if user['age'] > age_limit]
    
elif choice == '2':
    first_letter = input("Введите первую букву логина: ").strip().lower()
    if len(first_letter) != 1 or not first_letter.isalpha():
        print("Ошибка: нужно ввести одну букву.")
        exit()
    filtered = [user for user in users if user['login'].lower().startswith(first_letter)]
elif choice == '3':
    group_name = input("Введите название группы: ").strip()
    filtered = [user for user in users if user['group'] == group_name]
else:
    print("Неверный выбор типа сортировки.")
    exit()

filtered_sorted = sorted(filtered, key=lambda u: u['age'])

if not filtered_sorted:
    print("Нет пользователей, соответствующих критерию.")
else:
    print("Результат:")
    for user in filtered_sorted:
        print(f"Пользователь: '{user['login']}' возраст {format_age(user['age'])} , группа \"{user['group']}\"")


