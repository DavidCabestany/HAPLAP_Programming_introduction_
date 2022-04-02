def language_of_the_word(word):

    if word.endswith('tion'):
        return 'English!'
    elif word.endswith('cion'):
        return 'Spanish!'
    elif word.endswith('zio'):
        return 'Basque!'
    else:
        return "Ups... I don't know!"