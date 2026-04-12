
#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]


# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

seen_numbers = set()
result_pairs = {}

for i in range(len(mass)):
    num = mass[i]

    if num in seen_numbers:
        continue

    min_dist = float('inf')
    closest_pair = None

    for j in range(i + 1, len(mass)):
        if mass[j] == num:
            dist = j-1
            if dist < min_dist:
                min_dist = dist
                closest_pair = (i, j)

    if closest_pair:
        result_pairs[num] = closest_pair

    seen_numbers.add(num)

printed = set()
for num in mass: 
    if num not in printed:
        if num in result_pairs:
            idx1, idx2 = result_pairs[num]
            print(f"Для числа {num} мин. расстояние в массиве по индексам: {idx1} и {idx2}")
        else:
            print(f"Для числа {num} нет минимального расстояния т.к. элемент в массиве один")
        printed.add(num)

        