def counter(num):
    num += 1
    result = ''
    for i in range(num):
        i = str(i)
        result += i + '\n'
    return result