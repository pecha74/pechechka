# todo 1: Для игры "Морской бой" файл sea_battle.py написать создание игрового поля nxn

# todo 2: В игровой матрице nxn найти кол-во всех 1

#  Задачи решить через генераторы списков (списковые включения)
    
import random

def create_random_field(n, num_ships):
    
    field = [[0 for _ in range(n)] for _ in range(n)]
    
    all_ships = [(i, j) for i in range(n) for j in range(n)]
    
    ship_positions = random.sample(all_ships, num_ships)
    
    for i, j in ship_positions:
        field[i][j] = 1
    
    return field

def count_ships(field):
    
    return len([cell for row in field for cell in row if cell == 1])

if __name__ == "__main__":
    n = 5
    num_ships = 5
    
    battlefield = create_random_field(n, num_ships)
    
    print("Игровое поле:")
    for row in battlefield:
        print(row)
    
    ships_count = count_ships(battlefield)
    print(f"\nКоличество кораблей (единиц): {ships_count}")