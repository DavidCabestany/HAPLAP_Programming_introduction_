def double_factorial(pNum):
    if pNum == 0:
        return 1
    result = pNum
    for i in range(pNum-2,0,-2):
        result = result*i
    return int(result)
