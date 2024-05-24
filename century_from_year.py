def century(year):
    remainder = year % 100
    if remainder > 0 :
        return int(year / 100) + 1
    else:
        return int(year/100)