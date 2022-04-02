def hello_world():
    return "Hello World!"

def hello_my_friend(name):
    name = str(name)
    return 'Hello '+ name

def next_number(num):
    num = int(num)
    next_num = num + 1
    return next_num

def year_of_birth(age):
    age = int(age)
    birth = 2021 - age
    return birth

def degree_calculator(celsius):
    celsius = int(celsius)
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit
