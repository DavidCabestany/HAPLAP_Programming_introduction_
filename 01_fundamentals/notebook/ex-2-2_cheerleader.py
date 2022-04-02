def cheerleader(pTeam):
    rTeam = ''
    sTeam = ''
    for i in range(len(pTeam)):
        sTeam = sTeam + 'Give me a(n) ' + pTeam[i] + ', ' + pTeam[i]+ '!\n'
        #print(sTeam)
    rTeam = "What's that spell?" + '\n' + pTeam + '! ' + pTeam +'!'
    return sTeam + rTeam