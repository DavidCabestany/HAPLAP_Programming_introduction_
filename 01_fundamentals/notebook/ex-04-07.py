def word_in_the_book(path, word):
    rStr = ''
    file = open(path)
    count_w = 0
    count_l = 0
    for line in file:
        count_l += 1
        if word in line:
            count_w = line.count(word)
            rStr += 'Found in line: ' + str(count_l) + '\n'
    if count_w == 0:
        return 'Not found'
    file.close()

    return rStr 