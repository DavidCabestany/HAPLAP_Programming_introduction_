def steps(pLevel):
    
    pStart = pLevel+2
    rStep = '_'
    rJump = '\n'
    rDown = '|'
    rSpace = ' '
    rFinal = rStep*2+rJump
    #print(rStep*2+rSpace*2+rJump+rDown+rJump)
    if pLevel > 1:
        for i in range(1, pLevel):
            i = i*2
            rFinal = rFinal + rSpace*i +rDown + rStep + rJump
        return rFinal + rStep*(pLevel*2)+rDown
    return rFinal+rStep*2+rDown