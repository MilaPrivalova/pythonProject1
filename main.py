# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# x = int(input("Введите число от 1 до 7"))
# if x < 6:
#   print("нет")
# elif x == 6 or x == 7:
#   print("да")

 # Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# print()
# print('x, y, z')
# for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            print(x, y, z)
#            print((int(not (x or y or z))) == (not x and not y and not z))

#3.	Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

x = int(input("Введите число x "))
y = int(input("Введите число y "))
if x > 0 and y > 0:
    print(f'x = {x}; y = {y} -> I четверть')
elif x < 0 and y > 0:
    print(f'x = {x}; y = {y} -> II четверть')
elif x < 0 and y < 0:
    print(f'x = {x}; y = {y} -> III четверть')
elif x > 0 and y < 0:
    print(f'x = {x}; y = {y} -> IV четверть')
else:
    if x == 0 or y == 0:
        print('Некорректный ввод данных')
print()