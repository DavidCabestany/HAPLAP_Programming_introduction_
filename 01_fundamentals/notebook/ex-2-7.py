def lift_with_while(pCur, pTar):
    sTar = ''
    if pCur < pTar:
        while pTar > pCur:
            sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
            pCur +=1
        sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
        return sTar[:-1]
    if pCur > pTar:
        while pTar < pCur:
            sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
            pCur-=1
        sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
        return sTar[:-1]