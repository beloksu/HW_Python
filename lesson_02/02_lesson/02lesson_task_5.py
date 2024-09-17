def month_to_season(month):
    if month == 12 or 1 <= month <= 2:
        print("Зима")
    elif 3 <= month <= 5:
        print("Весна")
    elif 6 <= month <= 8:
        print("Лето")
    elif 9 <= month <= 11:
        print("Осень")
    else:
        print("Неверный номер месяца")


month = int(input("Введите число месяца: "))
month_to_season(month)
