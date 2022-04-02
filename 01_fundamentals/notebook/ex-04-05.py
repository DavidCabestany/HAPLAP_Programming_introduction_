def shout_requests(path):
    rStr = ''
    file = open(path)
    for line in file:
        rStr += line.upper()
    return rStr
 