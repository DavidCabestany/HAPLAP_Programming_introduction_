def usernames(path):
    import csv
    
    usr_lst = open(path, 'r')
    header = next(usr_lst)

    usr_DB = []
    
    count = 0
    rStr = ''
    f_name_s = ''
    f_name_c = ''
    midName = ''
    
    if header != None:
        for row in usr_lst:
            f_name, surname = row.split(' ', 1)
            f_name.lower()
            surname.lower()
            if '"' in f_name and '"' in surname:
                f_name, midName, surname = row.split(' ')
                f_name += midName
            if f_name not in usr_DB:
                usr_DB.append(f_name)
            elif f_name in usr_DB:
                f_name += surname[0]
                f_name_s = f_name
                f_name_c = f_name_s
                if f_name_s in usr_DB:
                    while f_name_c in usr_DB:
                        count+=1
                        f_name_c = f_name_s + str(count)
                    count = 0
                    usr_DB.append(f_name_c)
                else:
                    usr_DB.append(f_name_s)
        for el in usr_DB:
            rStr += el + '\n'
    return rStr.lower().strip().replace('"', '')
