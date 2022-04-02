def broken_keyboard(txt):
    a = '%%'
    e = '##'
    u = '###'
    txt = txt.replace(u, 'u')
    txt = txt.replace(a, 'a')
    txt = txt.replace(e, 'e')
    
    return txt
    