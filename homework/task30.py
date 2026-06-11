#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21

matrix = [[1, 2, 3], [4, 5, 6]]

def msum(matrix):
    return sum (x for row in matrix for x in row)

print(f"Сумма элементов матрицы равна: {msum(matrix)}")