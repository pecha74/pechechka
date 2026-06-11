# todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id. Номер по порядку (от 1 до 10); 
# – текст из списка algoritm;

# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# |-----------------|
# | 1 | "C4.5"      |
# | 2 | "k - means" |
# и т.д.

import csv

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

with open(r'C:/Users/User/OneDrive/Рабочий стол/Python/repo/Homework/algoritm.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['id', 'algoritm'])
    
    for i, name in enumerate(algoritm, start=1):
        writer.writerow([i, name])

print('Файл успешно создан!')