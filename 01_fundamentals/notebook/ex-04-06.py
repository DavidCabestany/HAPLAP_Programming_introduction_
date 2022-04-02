def virus(path):
    rStr = ''
    file = open(path)
    for line in file:
        if line[:5] == 'VIRUS':
            rStr = rStr
        else:
            rStr += line
    return rStr 