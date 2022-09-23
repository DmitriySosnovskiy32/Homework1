print('Задача 1:')
print('Обычный список:')
list_favorite_colors = ['красный', 'зеленый', 'белый', 'черный', 'розовый', 'желтый']
print(list_favorite_colors)

print('Переделанный список:')
del list_favorite_colors[0]
del list_favorite_colors[3:5]
print(list_favorite_colors)

print('Задача 2:')
first_favorite_color = set(['белый', 'жёлтый'])
print('1 список :', first_favorite_color)
second_favorite_color = set(['фиолетовый', 'синий'])
print('2 список', second_favorite_color)
all_favorite_colors = first_favorite_color.union(second_favorite_color)
print('Все любимые цвета (два списка):', all_favorite_colors)

dict_clothes_number_tableware = {'clothes': 'pants', 2: [5, 6, 8], 'tableware': 'plate'}
print('Задача 3:')
print('Словарь: ', dict_clothes_number_tableware)
raspakovka = dict_clothes_number_tableware.items()
print('Распакованный словарь по парам(ключ-значение): ', raspakovka)

# 001
print('Введите Ваше имя:')
name = str(input())
print('Привет,', name, ', хорошего Вам дня!')

# 002
print('Введите вашу фамилию:')
first_name = str(input())
print('Привет,', name, first_name, 'хорошего вам дня!')

# 003
print('What do you call a bear with no teeth? \n"A gummy bear!"')

# 004
print('Пожалуйста, введите первое число')
first_numder = int(input())
print(' Пожалуйста, введите второе число')
second_numder = int(input())
summa_numbers = first_numder + second_numder
print('Сумма чисел =', summa_numbers)


