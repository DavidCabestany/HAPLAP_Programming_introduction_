def red_and_blue_cars(cars):
    rCars = cars.split(' ')
    blue = 0
    red = 0
    
    for car in rCars:
        if car == 'blue':
            blue += 1
        if car == 'red':
            red += 1
        
    return red,blue