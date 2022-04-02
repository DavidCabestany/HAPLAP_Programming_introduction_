def secret_message(pMessage):
    message = pMessage.split(' ')
    rSecret = []
    for word in message:
        if word[0].isupper():
            rSecret.append(word)
    rSecret.reverse()
    #rSecret = str(rSecret)
    rFin = ''
    for el in rSecret:
        rFin = rFin + ' ' + el
    
    return rFin.lower().strip()