def lift_up_and_down(pCur, pTar):
    
    sTar = ''
    if pTar <= pCur:
        for i in range(pCur, pTar, -1):
            #if pCur >= pTar:
            sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
            pCur = pCur -1
        sTar = sTar + 'Floor number: ' + str(pCur)
    if pTar > pCur:
        pTar += 1
        for i in range(pCur, pTar, 1):
            if pCur < pTar:
                sTar = sTar + 'Floor number: ' + str(pCur) + '\n'
                pCur +=1
        sTar = sTar[:-1]
    return sTar