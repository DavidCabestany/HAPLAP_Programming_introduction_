def cars_colours():
    cars = {}
    rStr = ''
    usr_inp = input('')
    while usr_inp != '':
        if usr_inp in cars:
            cars[usr_inp] += 1
        else:
            cars[usr_inp] = 1
        usr_inp = input('')
    for car in  sorted(cars):
        rStr += car + ' ' + str(cars[car]) + '\n'
    return rStr