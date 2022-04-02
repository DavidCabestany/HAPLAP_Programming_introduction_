def positive_and_even(num):
    user_num = int(num)
    odd = user_num % 2
    if user_num < 0:
        return "The number entered is not positive"
    elif odd == 1:
        return "The number entered is positive and odd"
    elif odd == 0:
        return"The number entered is positive and even"
    