def scrabble_game(word):
    eus = open('data/points_eu.txt')
    eng = open('data/points_en.txt')
    
    eus_dic = {}
    eng_dic = {}
    
    eus_score = 0
    eng_score = 0
    
    for line in eus:
        key, value = line.split()
        eus_dic[value.lower()] = int(key)
    
    for line in eng:
        key, value = line.split()
        eng_dic[value.lower()] = int(key)
    
    for char in word:
        eus_score += eus_dic.get(char)
        
    for char in word:
        eng_score += eng_dic.get(char)
        
        
    return  eus_score, eng_score