def is_year_leap(year):
    if year % 4 == 0:
        print(f"год {year}: True")
    else:
        print(f"год {year}: False")


is_year_leap(2004)
is_year_leap(2003)
is_year_leap(1999)
is_year_leap(1234)
is_year_leap(8888)
