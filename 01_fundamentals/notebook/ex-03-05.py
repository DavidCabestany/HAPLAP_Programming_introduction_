def order_students_names(names):
    rList = ''
    or_names = names.split(' ')
    or_names.sort()
    for el in or_names:
        rList = rList + '\n'+el
    return 'List of students:'+rList
    