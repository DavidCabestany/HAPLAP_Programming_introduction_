def words_frequency():
    words = {}
    rStr = ''
    usr_inp = input('')
    while usr_inp != '':
        for i in usr_inp.split(' '):
            if i in words:
                words[i] += 1
            else:
                words[i] = 1
        usr_inp = input('')
    for word in sorted(words, reverse = True):
        rStr += word + ' ' + str(words[word]) + '\n'
    return rStr.strip()