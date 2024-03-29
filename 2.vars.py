# Типы данных

# Динамически и строго типизированный язык

# Целочисленные значения (int, integer)
my_int = 5

# Числа с плавающей точкой (вещественные значения) (float)
my_float = 3.14

# Строковые данные (текстовая строка, слова, символы) (str, string)
my_string = 'Hello, world'
my_text = """
многострочный
текст
"""

# Способы форматирования строк

# Конкатенация строк
str_1 = 'Hello'
str_2 = 'world'
str_3 = 'Number '
num_1 = 3

# "старый" способ
str_5 = str_1 + ', ' + str_2

str_6 = str_3 + str(num_1)

# "новый" способ (f-string)
str_7 = f'{str_1}, {str_2}'
str_8 = f'{str_3} {num_1}'

# Булевы типы данных (boolean) (true | false)
ool_1 = True  # "истина", логическая 1
bool_2 = False  # "ложь", логический 0


# Арифметические операции

a = 10
b = 3

# Сложение
result = a + b

# Вычитание
result = a - b

# Умножение
result = a * b

# Обычное деление (всегда возвращает числа с плавающей точкой)
b = 3
result = a / b

# Целочисленное деление (всегда возвращает целую часть)
result = a // b

# Деление по остатку
result = a % b
