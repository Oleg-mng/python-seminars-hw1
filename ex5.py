# Задача 5
# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

print('введите координаты точки A: ')
x1=float(input('введите x1: '))
y1=float(input('введите y1: '))
#A=[x1,y1]
print('введите координаты точки B: ')
x2=float(input('введите x2: '))
y2=float(input('введите y2: '))
#B=[x2,y2]
distance2d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print('расстояние между точками в 2D пространстве: ', round(distance2d,5))
