def guess_game():
    gWord = 'chocolate'
    pFood = input("What is my favourite food?")
    while pFood != gWord:
        print('You are wrong.')
        pFood = input("What is my favourite food?")   
    print('You guessed it')
    return
