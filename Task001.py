# Напишите программу, которая принимает на вход два числа
# и проверяет является ли одно число квадратом другого.

def square(a, b):
    if a == b**2:
        print(f"Да, {a} является квадратом {b}")
    else:
        print(f"Нет, {a} не является квадратом {b}")

square(4, 2)