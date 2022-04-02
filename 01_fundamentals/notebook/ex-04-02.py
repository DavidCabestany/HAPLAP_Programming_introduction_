def favourite_colour():
    colours = {}
    rStr = ''
    usr_inp = input('')
    while usr_inp != '':
        name, colour = usr_inp.split(' ')
        
        colours[name] = colour
        #rStr += str(name) + ' ' + str(colour) + '\n'
        usr_inp = input('')
    #ColorSort = sorted(colours)
    for name in sorted(colours):
        rStr += name + ' ' + colours[name] + '\n'
            #rStr += str(el) + ' ' + str(i) + '\n'
    return rStr.strip()
    