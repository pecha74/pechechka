# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.

# # Пример:
# game_field = []
# # нужно заменить статическую инициализацию списка на динамическую с помощью lambda выражения.
# row_one   = [0, 0, 0, 1, 0]
# row_two   = [0, 0, 0, 1, 0]
# row_three = [0, 1, 0, 0, 0]
# row_four  = [0, 0, 0, 1, 0]
# row_five  = [0, 0, 0, 1, 0]

# game_field.append(row_one)
# game_field.append(row_two)
# game_field.append(row_three)
# game_field.append(row_four)
# game_field.append(row_five)
# i = 0  # вхождение в первый массив
# j = 3  # вхождение в 4-ый элемент текущего массива
# # доступ к элементам двухмерного массива
# print(game_field[i][j])


import random

gen_cell = lambda: random.choice([0, 1])

game_field = []

for i in range(5):
    row = []
    for i in range(5):
        row.append(gen_cell())
    game_field.append(row)

total_ships = sum(sum(row) for row in game_field)

print("Игровое поле готово")
print("Количество кораблей:", total_ships)
print("Поле:")

for row in game_field:
    print(row)

while total_ships > 0:
    try:
        i = int(input("Введите номер строки (0-4): "))
        j = int(input("Введите номер столбца (0-4): "))
        if not (0 <= i < 5 and 0 <= j < 5):
            print("Координаты вне диапазона! Введите число от 0 до 4")
            continue

        if game_field[i][j] == 1:
            print("Попали!")
            game_field[i][j] = 0
            total_ships -= 1
            print(f"Осталось кораблей: {total_ships}")
        else:
            print("Промазали!")

        print("Текущее поле:")
        for row in game_field:
            print(row)

    except ValueError:
        print("Введите целое число!")

print("Поздравляем! Вы выиграли!")