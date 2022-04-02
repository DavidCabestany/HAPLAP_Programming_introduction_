def text_info(txt):
    txt_lst = txt.split(' ')
    txt_len = len(txt)
    kuku = 'kuku'
    kukus = txt.lower().count('kuku')
    kukuak = "Number of kuku's:"
    count_l = 0
    count_u = 0
    up = ''
    low = ''
    both = ''
    for ch in txt:
        if ch.islower():
            count_l += 1
        if ch.isupper():
            count_u += 1
            
    if count_u > 0:
        up = 'In upper case' 
    if count_l > 0:
        low = 'In lower case'
    if count_u > 0 and count_l > 0:
        up = ''
        low = ''
        both = 'Both lower and upper case'
    #for word in txt_lst:
        #for kuku in word.lower():
            #kukus += 1
    if int(kukus) == 0:
        kukuak = ''
        kukus = 'No kuku this way'
    return 'Size of the text: ' + str(txt_len) + '\n' + kukuak + str(kukus) + '\n' + up + low + both