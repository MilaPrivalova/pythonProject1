х = int(input("Введите число:"))
sum = 0
while х > 0:
 number = х % 10
 sum = sum + number
 х = х // 10
print("Сумма цифр =", sum)