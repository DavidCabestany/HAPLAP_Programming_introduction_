def word2sms(word:str):
    rFin = ''
    dos = ('a', 'b', 'c')
    tres = ('d', 'e', 'f')
    cuatro = ('g', 'h', 'i')
    cinco = ('j', 'k', 'l')
    seis = ('m', 'n', 'o')
    siete = ('p', 'q', 'r', 's')
    ocho = ('t', 'u', 'v')
    nueve = ('w', 'x', 'y', 'z')
    Dos = dict.fromkeys(dos, '2')
    Tres = dict.fromkeys(tres, '3')
    Cuatro = dict.fromkeys(cuatro, '4')
    Cinco = dict.fromkeys(cinco, '5')
    Seis = dict.fromkeys(seis, '6')
    Siete = dict.fromkeys(siete, '7')
    Ocho = dict.fromkeys(ocho, '8')
    Nueve = dict.fromkeys(nueve, '9')
    dic = {**Dos, **Tres, **Cuatro, **Cinco, **Seis, **Siete, **Ocho, **Nueve}
    for ch in word.lower():
        ch = dic.get(ch)
        rFin += ch
    return rFin