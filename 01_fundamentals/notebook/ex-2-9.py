def look_for_factors(pNum):
    result = ''
    for i in range(1, pNum+1):
        if pNum % i == 0:
            result = result + str(i) + '\n'
    return result