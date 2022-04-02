def rainy_days(rainy):
    days = rainy.split(' ')
    if rainy == '':
        return 7
    return 7-len(days)