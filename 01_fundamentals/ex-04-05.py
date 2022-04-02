def shout_requests(path):
    rStr = ""
    fin = open(path)
    for line in fin:
        rStr = rStr + line.upper()
    #fin.close()
    return rStr.strip()

    