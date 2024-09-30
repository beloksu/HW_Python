def month_to_season(month):
    if 1 <= month <= 2:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    elif 12 <= month <= 12:
        return "Зима"
    else:
        return "Неверный номер месяца"