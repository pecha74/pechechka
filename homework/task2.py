# todo: Преобразуйте переменную age и foo в число
age = "23"
try:
    age_num = int(age)
    print(f"age преобразовано в число: {age_num}")
except ValueError:
    print(f"Невозможно преобразовать age ('{age}') в число")

foo = "23abc"
try:
    foo_num = int(foo)
    print(f"foo преобразовано в число: {foo_num}")
except ValueError:
    print(f"Невозможно преобразовать foo {foo} в число")

# Преобразуйте переменную age в Boolean
age = "123abc"
age_bool = bool(age)
print(f"age преобразовано в Boolean: {age_bool}")

# Преобразуйте переменную flag в Boolean
flag = 1
flag_bool = bool(flag)
print(f"flag преобразовано в Boolean: {flag_bool}")

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one_bool = bool(str_one)
print(f"str_one преобразовано в Boolean: {str_one_bool}")
str_two_bool = bool(str_two)
print(f"str_two преобразовано в Boolean: {str_two_bool}")

# Преобразуйте значение 0 и 1 в Boolean
a = 0
b = 1
a_bool = bool(a)
b_bool = bool(b)
print(f"a преобразовано в Boolean: {a_bool}")
print(f"b преобразовано в Boolean: {b_bool}")

# Преобразуйте False в строку
bool_value = False
str_value = str(bool_value)
print(f"False преобразовано в строку: {str_value}")
print(type(str_value))