def palindromes(word):
    word = word.replace(' ', '')
    drow = word[::-1]
    
    if word == drow:
        return 'Good!!'
    if word != drow:
        return 'No, you missed it...'