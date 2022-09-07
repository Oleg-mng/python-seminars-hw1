# Задача 2.
# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
print (' ')
print('все возможные варианты предикат: ')
print('проверка всех 8-ти вариантов на истинность утверждения:')
print(' ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
count = 0
a=0
for x in range(2):
    for y in range(2):
        for z in range(2):
            # print(x, ' ', y, ' ', z, '|')
            count += 1
            print('Вариант', count)
            if x == 0 and y == 0 and z == 0: 
                a=1
            else: a=0
            if x == 0 and y == 0 and z == 0 or x == 1 and y == 1 and z == 1:
                b=1
            else: b=0
            if a==b:   
                print(x, ' ', y, ' ', z,  '|' , a, '=', b)
                print('Вариант', count, 'Утверждение верно')
            else:  
                print(x, ' ', y, ' ', z,  '|' , a, '!=', b)
                print('Вариант', count, 'Утверждение Не верно')
