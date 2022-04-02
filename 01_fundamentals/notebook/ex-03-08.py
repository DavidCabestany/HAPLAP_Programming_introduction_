def how_many_words():
    words = input('')
    new_words = []
    rList = []
    while words != '':
        rList.append(words)
        words = input('')
    for word in rList:
        if word not in new_words:
            new_words.append(word)
    return len(new_words)