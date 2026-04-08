
###банк хранит деньги
#изначально на счету 1000 денег
# Управление через меню, путём ввода текста 1-баланс, 2-пополнить счёт, 3-вывести, 4-выход
#написать функции для всех действий со счётом. 
# ##

balance = 1000

def showMenu():
   print(f'''
          #Меню
          1.Проверить баланс
          2.Пополнить счёт
          3.Вывести со счёта
          4.Выход
            ''')

def deposit():
    global balance
    amount = int(input("сколько прибаавить?"))
    balance = balance + amount
    print(f'Счет увеличился, баланс: {balance}')

def withdraw():
    global balance
    amount = int(input("сколько убавить?"))
    balance = balance - amount
    print(f'Счет уменьшился, баланс: {balance}')


def chooseMenu(n):
  global balance
  match n:
    case 1:
      print(balance)
    case 2:
      deposit()
    case 3:
      withdraw()
            

def main():
   
  while True:
      
    showMenu()

    inp = int(input("Выберите пункт меню: "))
    if type(inp) != type(1):
      print("введи число")
      inp = int(input("Выберите пункт меню: "))

    chooseMenu(inp)

    if inp ==4:
      print("Выход из программы")
      break

main()
