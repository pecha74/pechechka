
#my
#function две разные переменные
#способ написания двух переменных для def через _ (ниж подчеркивание) или вторая функция пишется с большой буквы myFunction
def nameFunc ():
    x = 1+1
    print("шаг 1")
    
    return x

print(nameFunc())
#если не указыватть () nameFunc просто ссылается на def. Это нужно для ...

result = 0

def summ (a, b=0): #парметры 
    result = a + b
    print(result)
    return result

def parser(name, age, salary, position, e, f):
    print(name, age, salary, position, e, f)
    # result = list(a, b, c, d, e, f)
    return result

p1 = parser(name="Ivan", age=44, position="director", salary=100, e=0, f=0) #важно указать присвоение!!!
print(p1)


x1 = summ(6) #аргументы
x2 = summ(7, 3) 
x3 = summ(99, 8) 

print(x1, x2, x3)


def raznost(a, b, *args):
    print(args)
    result = a - b
    return result

raznost(5, 7, 8, 9)


def miltiple(**kwargs):
    print(kwargs)
    a = kwargs['first']
    b = kwargs['second']
    result = a * b
    return result

print(miltiple(first=1, second=4, third=4))

result = 0

def summ(a, b=0):
    #scope = область видимости [result, a, b]
    global result 
    print("---", result)
    result = a + b
    print(result)
    return result

print(summ(1,2))


