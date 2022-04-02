def lift_only_up(pCur, pTar):
    pTar += 1
    sTar = ''
    for i in range(pCur, pTar):
        if pCur < pTar:
            sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
            pCur +=1
    return sTar