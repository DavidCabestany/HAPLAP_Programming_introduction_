def how_many_words():
    result = 0
    words = []
    line = input("Word: ")
    while line != "":
        if line in words:
            continue
        else:
            words.append(line)
            result = result + 1
        line = input("Word: ")
    return result
