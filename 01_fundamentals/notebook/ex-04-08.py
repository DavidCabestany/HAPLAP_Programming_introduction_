def spanish_elephant_in_file(path):
    rStr = ''
    file = open(path)
    
    count_l = 0
    for line in file:
        count_l += 1
        if line.count('e') > 2 and line.count('l') > 0 and line.lower().count('f') > 0 and line.count('a') > 0 and line.count('n') > 0 and line.count('t') > 0:
            rStr += 'Spanish elephant in this line: ' + str(count_l) + '\n'
    file.close()

    return rStr