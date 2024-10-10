import math


def square(x):
    return math.ceil(x * x)


number = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата = {square(number)}")
