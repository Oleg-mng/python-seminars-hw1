# Задача 1.
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
day_of_week = int(input('введите день недели (от 1 до 7) в виде цифры: '))
if (day_of_week == 6) or (day_of_week == 7):
    print('-> да')
else:
    print('-> нет')
