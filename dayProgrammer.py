def dayOfProgrammer(year):
    if year == 1918:
        day = 26
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        day = 12
    else:
        day = 13
    return f"{day}.09.{year}"

